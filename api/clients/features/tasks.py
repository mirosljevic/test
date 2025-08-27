from typing import Optional
from requests import Session
from time import sleep
from models import Operator
from logger import log
from api.endpoints.workflow.workflow_cc import get_filters, get_tasks, claim_task, complete_task


class OperatorTasksApi:
    def __init__(self, session: Optional[Session] = None, operator: Optional[Operator] = None):
        self.session = session
        self.operator = operator

    def get_tasks(self, player_id, filter_name="Player Management - Player's Tasks"):
        filters = get_filters(session=self.session, validate_response=True).json()
        filter_id = [f for f in filters if f["name"] == filter_name][0]["id"]

        tasks = get_tasks(session=self.session, filter_id=filter_id,
                          player_id=player_id, validate_response=True).json()['pageItems']
        log.debug(f"Tasks Found (player id {player_id}): {[task['name'] for task in tasks]}")
        return tasks

    def wait_for_task(self, task_name, player_id, retries=20, timeout=2):
        for _ in range(retries):
            tasks = self.get_tasks(player_id)
            if any(task["name"] == task_name for task in tasks):
                log.info(f"Task {task_name} found for player {player_id}")
                return True
            log.warning(f"Task {task_name} not found for player {player_id}. Retrying...")
            sleep(timeout)
        return False

    def claim_and_complete_task(self, task_name, player_id, payload):
        success = self.wait_for_task(task_name, player_id)
        if success:
            tasks = self.get_tasks(player_id)
            task_id = [x["id"] for x in tasks if x["name"] == task_name][0]
            claim_task(session=self.session, task_id=task_id, validate_response=True)
            complete_task(session=self.session, task_id=task_id, payload=payload, validate_response=True)
            return True
        else:
            log.error(f"Task {task_name} not found for player {player_id}")
            raise
