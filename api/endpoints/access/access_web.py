from api.executor import api
from environment import hosts


@api
def get_access_attributes(session, **kwargs):
    return {
        "session": session,
        "host": hosts.gateway_web,
        "endpoint": "/web/access/rest/v1/access-attributes",
        "method": "get",
        **kwargs
    }


@api
def get_user_permissions(session, user_id=None, **kwargs):
    endpoint = "/web/access/rest/v1/permissions"
    params = {
        "user_id": user_id,
    }

    return {
        "session": session,
        "host": hosts.gateway_web,
        "endpoint": endpoint,
        "method": "get",
        "params": params,
        **kwargs
    }


@api
def get_role_permissions(session, role_id, **kwargs):
    return {
        "session": session,
        "host": hosts.gateway_web,
        "endpoint": f"/web/access/rest/v1/roles/{role_id}/permissions",
        "method": "get",
        **kwargs
    }


@api
def check_user_access(session, resource, action, **kwargs):
    return {
        "session": session,
        "host": hosts.gateway_web,
        "endpoint": "/web/access/rest/v1/check",
        "method": "post",
        "data": {"resource": resource, "action": action},
        **kwargs
    }


@api
def get_user_roles(session, **kwargs):
    return {
        "session": session,
        "host": hosts.gateway_web,
        "endpoint": "/web/access/rest/v1/user/roles",
        "method": "get",
        **kwargs
    }
