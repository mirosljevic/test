from api.executor import api
from environment import hosts


@api
def get_filters(session, **kwargs):
    return {
        "session": session,
        "host": hosts.cc,
        "endpoint": "/cc/workflow/rest/v1/filters",
        **kwargs
    }


@api
def get_tasks(session, filter_id, player_id=None, **kwargs):
    return {
        "session": session,
        "host": hosts.cc,
        "endpoint": f"/cc/workflow/rest/v1/filters/{filter_id}/tasks",
        "params": {"playerId": player_id} if player_id else None,
        **kwargs
    }


@api
def claim_task(session, task_id, **kwargs):
    return {
        "session": session,
        "host": hosts.cc,
        "endpoint": f"/cc/workflow/rest/v1/tasks/{task_id}/claim",
        "method": "POST",
        "json": {"params": {}},
        **kwargs
    }


@api
def complete_task(session, task_id, payload, **kwargs):
    return {
        "session": session,
        "host": hosts.cc,
        "endpoint": f"/cc/workflow/rest/v1/tasks/{task_id}/complete",
        "method": "POST",
        "json": payload,
        **kwargs
    }
