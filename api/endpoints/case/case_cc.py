from api.executor import api
from environment import hosts


@api
def get_cases_for_player(session, player_id=None, running_cases=None, page_number=None, page_size=None,
                         sort_by=None, sort_order=None, **kwargs):
    params = {
        "playerId": player_id,
        "runningCases": running_cases,
        "pageNumber": page_number,
        "pageSize": page_size,
        "sortBy": sort_by,
        "sortOrder": sort_order
    }
    return {
        "session": session,
        "method": "GET",
        "host": hosts.cc,
        "params": params,
        "endpoint": "/cc/case/rest/v1/cases",
        **kwargs
    }


@api
def reject_case(session, case_id, **kwargs):
    return {
        "session": session,
        "method": "POST",
        "host": hosts.cc,
        "endpoint": f"/cc/case/rest/v1/cases/{case_id}/reject",
        **kwargs
    }


@api
def set_case_status(session, case_id, status=None, **kwargs):
    payload = {}
    if status is not None:
        payload["status"] = status
    return {
        "session": session,
        "method": "PUT",
        "host": hosts.cc,
        "endpoint": f"/cc/case/rest/v1/cases/{case_id}/status",
        "json": payload,
        **kwargs
    }


@api
def link_document_to_case(session, case_id, document_type, sub_type, confidential=None, document_id=None, add_file=None,
                          payment_method_id=None):
    files = {
        'caseId': (None, str(case_id)),
        'type': (None, document_type),
        'subType': (None, sub_type),
        "documentId": (None, str(document_id)) if document_id is not None else None,
    }
    if payment_method_id is not None:
        files['paymentMethodId'] = (None, str(payment_method_id))
    if confidential is not None:
        files['confidential'] = (None, str(confidential))
    if add_file is not None:
        files["file"] = ("icon.png", open("files/images/sample.png", "rb"), "image/png")

    return {
        "session": session,
        "method": "POST",
        "host": hosts.cc,
        "endpoint": f"/cc/case/rest/v1/cases/{case_id}/documents",
        "files": files,
        "content_type": None
    }


@api
def list_cases_by_business_object(session, external_id=None, object_type=None, page_number=None, page_size=None,
                                  sort_by=None, sort_order=None, **kwargs):
    params = {
        "externalId": external_id,
        "type": object_type,
        "pageNumber": page_number,
        "pageSize": page_size,
        "sortBy": sort_by,
        "sortOrder": sort_order
    }
    return {
        "session": session,
        "method": "GET",
        "host": hosts.cc,
        "params": params,
        "endpoint": "/cc/case/rest/v1/cases/business-objects",
        **kwargs
    }


@api
def get_case_details(session, case_id, include_snapshots=None, include_related=None, include_history=None, **kwargs):
    params = {
        "includeSnapshots": include_snapshots,
        "includeRelated": include_related,
        "includeHistory": include_history
    }
    return {
        "session": session,
        "method": "GET",
        "host": hosts.cc,
        "params": params,
        "endpoint": f"/cc/case/rest/v1/cases/{case_id}",
        **kwargs
    }


@api
def get_case_history(session, case_id):
    return {
        "session": session,
        "method": "GET",
        "host": hosts.cc,
        "endpoint": f"/cc/case/rest/v1/cases/{case_id}/history"
    }


@api
def request_document_for_case(session, case_id, payment_method_id=None, player_id=None, doc_type=None, doc_sub_type=None):
    payload = {
        "playerId": player_id,
        "paymentMethodId": payment_method_id,
        "type": doc_type,
        "subType": doc_sub_type
    }
    return {
        "session": session,
        "method": "POST",
        "host": hosts.cc,
        "endpoint": f"/cc/case/rest/v1/cases/{case_id}/document-requests",
        "json": payload
    }


@api
def relate_cases(session, case_id, related_case_id):
    payload = {
        "relatedCaseId": related_case_id
    }
    return {
        "session": session,
        "method": "POST",
        "host": hosts.cc,
        "endpoint": f"/cc/case/rest/v1/cases/{case_id}/relate",
        "json": payload
    }


@api
def list_related_cases(session, case_id):
    return {
        "session": session,
        "method": "GET",
        "host": hosts.cc,
        "endpoint": f"/cc/case/rest/v1/cases/{case_id}/related"
    }


@api
def create_case_file(session, case_id):
    return {
        "session": session,
        "method": "POST",
        "host": hosts.cc,
        "endpoint": f"/cc/case/rest/v1/cases/{case_id}/casefiles"
    }


@api
def list_case_snapshots(session, case_id):
    return {
        "session": session,
        "method": "GET",
        "host": hosts.cc,
        "endpoint": f"/cc/case/rest/v1/cases/{case_id}/snapshots"
    }
