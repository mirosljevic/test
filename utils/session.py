from re import search
from logger import log


def get_session_state(response):
    cookies = response.headers['set-cookie']
    match = search(r'AUTH_SESSION_ID=([^;]+)', cookies)
    session_state = match.group(1).split('.')[0]
    log.debug(f"session_state: {session_state}")
    return session_state