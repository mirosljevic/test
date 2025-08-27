from api.executor import api
from environment import hosts


@api
def get_list_of_audit_logs_case(access_token, object_type=None, object_id=None, date_from=None, date_to=None, rev=None,
                                include_only_changes=None, **kwargs):
    params = {
        "objectType": object_type,
        "objectId": object_id,
        "from": date_from,
        "to": date_to,
        "rev": rev,
        "includeOnlyChanges": include_only_changes
    }

    return {
        "host": hosts.api,
        "endpoint": "/api/case/rest/v1/audit-history",
        "bearer_token": access_token,
        "params": params,
        **kwargs
    }


@api
def get_list_of_cases(access_token, player_id=None, criticality=None, priority=None, status=None,
                      running_cases=None, case_type=None, case_ids=None, page_number=None, page_size=None,
                      sort_by=None, sort_order=None, **kwargs):
    params = {
        "playerId": player_id,
        "criticality": criticality,
        "priority": priority,
        "status": status,
        "runningCases": running_cases,
        "type": case_type,
        "caseIds": case_ids,
        "pageNumber": page_number,
        "pageSize": page_size,
        "sortBy": sort_by,
        "sortOrder": sort_order
    }

    return {
        "host": hosts.api,
        "endpoint": "/api/case/rest/v1/cases",
        "params": params,
        "bearer_token": access_token,
        **kwargs
    }


@api
def get_case_details(access_token, case_id):
    return {
        "host": hosts.api,
        "endpoint": f"/api/case/rest/v1/cases/{case_id}",
        "bearer_token": access_token
    }


@api
def get_list_of_case_id_snapshots(access_token, case_id):
    return {
        "host": hosts.api,
        "endpoint": f"/api/case/rest/v1/cases/{case_id}/snapshots",
        "bearer_token": access_token
    }


@api
def get_case_snapshot_details(access_token, case_id, snapshot_id):
    return {
        "host": hosts.api,
        "endpoint": f"/api/case/rest/v1/cases/{case_id}/snapshots/{snapshot_id}",
        "bearer_token": access_token
    }


@api
def update_case_status(access_token, case_id, status):
    payload = {
        "status": status
    }
    return {
        "host": hosts.api,
        "method": "PUT",
        "endpoint": f"/api/case/rest/v1/cases/{case_id}/status",
        "bearer_token": access_token,
        "json": payload
    }


@api
def create_case(access_token, created_by, criticality, name, opening_reason, parent_id, player_id, priority, trigger,
                case_type,
                workflow_instance_id):
    payload = {
        "createdBy": created_by,
        "criticality": criticality,
        "name": name,
        "openingReason": opening_reason,
        "parentId": parent_id,
        "playerId": player_id,
        "priority": priority,
        "trigger": trigger,
        "type": case_type,
        "workflowInstanceId": workflow_instance_id
    }
    return {
        "host": hosts.api,
        "method": "POST",
        "endpoint": "/api/case/rest/v1/cases",
        "bearer_token": access_token,
        "json": payload
    }


@api
def close_case(access_token, case_id, resolution):
    payload = {
        "resolution": resolution
    }
    return {
        "host": hosts.api,
        "method": "POST",
        "endpoint": f"/api/case/rest/v1/cases/{case_id}/close",
        "bearer_token": access_token,
        "json": payload
    }


@api
def reject_case(access_token, case_id):
    return {
        "host": hosts.api,
        "method": "POST",
        "endpoint": f"/api/case/rest/v1/cases/{case_id}/reject",
        "bearer_token": access_token
    }


@api
def create_case_document_link(access_token, case_id, doc_type, doc_sub_type, confidential, document_id=None, add_file=None):
    files = {
        "type": (None, doc_type),
        "subType": (None, doc_sub_type),
        "confidential": (None, confidential),
        "documentId": (None, document_id) if document_id is not None else None,
    }
    if add_file is not None:
        files["file"] = ("icon.png", open("files/images/sample.png", "rb"), "image/png")
    return {
        "host": hosts.api,
        "method": "POST",
        "endpoint": f"/api/case/rest/v1/cases/{case_id}/documents",
        "bearer_token": access_token,
        "content_type": None,
        "files": files
    }


@api
def upload_document_to_case(access_token, case_id, doc_type, doc_sub_type, confidential, file_location):
    params = {}
    return {
        "host": hosts.api,
        "method": "POST",
        "endpoint": f"/api/case/rest/v1/cases/{case_id}/documents",
        "bearer_token": access_token,
        "params": params,
        "files": {
            "type": (None, doc_type),
            "subType": (None, doc_sub_type),
            "confidential": (None, confidential),
            "file": ("icon.png", open(file_location, "rb"), "image/png"),
        },
        "content_type": "multipart/form-data",
    }


@api
def unlink_case_and_document(access_token, case_id, document_id):
    return {
        "host": hosts.api,
        "method": "DELETE",
        "endpoint": f"/api/case/rest/v1/cases/{case_id}/documents/{document_id}",
        "bearer_token": access_token
    }


@api
def create_case_entry(access_token, case_id, object_id=None, entry_type=None):
    payload = {
        "objectIds": object_id,
        "type": entry_type
    }
    return {
        "host": hosts.api,
        "method": "POST",
        "endpoint": f"/api/case/rest/v1/cases/{case_id}/entries",
        "bearer_token": access_token,
        "json": payload
    }


@api
def relate_cases(access_token, case_id1, case_id2):
    payload = {
        "relatedCaseId": case_id2
    }
    return {
        "host": hosts.api,
        "method": "POST",
        "endpoint": f"/api/case/rest/v1/cases/{case_id1}/relate",
        "bearer_token": access_token,
        "json": payload
    }


@api
def create_case_snapshot(access_token, case_id, object_type, data_value=None):
    payload = {
        "type": object_type,
    }

    if data_value is not None:
        payload["data"] = '{"value":' + data_value + '}'

    return {
        "host": hosts.api,
        "method": "POST",
        "endpoint": f"/api/case/rest/v1/cases/{case_id}/snapshots",
        "bearer_token": access_token,
        "json": payload
    }
