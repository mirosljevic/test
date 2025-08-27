from functools import wraps
from typing import Callable, Dict, Any
from requests import Response
from logger import log

from .executor import ApiExecutor


def api(func: Callable[..., Dict[str, Any]]) -> Callable[..., Response]:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Response:
        log.debug(25*"*" + " Api Request " + 25*"*")
        func_name = getattr(func, "__name__", str(func))
        try:
            request_params = func(*args, **kwargs)
            if not isinstance(request_params, dict):
                raise ValueError(
                    f"Function {func_name} must return a dictionary with request parameters, "
                    f"got {type(request_params)}"
                )
            executor = ApiExecutor(**request_params)
            response = executor.execute()
            log.debug(63*"*")
            return response
        except Exception as e:
            log.debug(63 * "*")
            log.error(f"Error in @api decorator for {func_name}: {e}")
            raise

    return wrapper
