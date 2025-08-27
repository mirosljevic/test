from api.executor import api
from environment import hosts


@api
def upload_document(session, document_type, file_location, **kwargs):
    return {
        "session": session,
        "method": "post",
        "host": hosts.gateway_web,
        "endpoint": "/web/document/rest/v1/documents",
        "files": {
            "type": (None, document_type),
            "file": ("icon.png", open(file_location, "rb"), "image/png"),
        },
        "content_type": None,
        **kwargs
    }


@api
def get_requests(session, **kwargs):
    return {
        "session": session,
        "method": "get",
        "host": hosts.gateway_web,
        "endpoint": "/web/document/rest/v1/requests",
        **kwargs
    }
