from typing import Optional, Dict, Any, Union
import requests
from urllib.parse import urljoin
from requests import Response
from logger import log


class ApiExecutor:
    def __init__(
        self,
        host: Optional[Dict[str, Any]] = None,
        endpoint: Optional[Dict[str, Any]] = None,
        method: str = "get",
        json: Optional[Dict[str, Any]] = None,
        data: Optional[Union[Dict[str, Any], str]] = None,
        params: Optional[Dict[str, Any]] = None,
        bearer_token: Optional[str] = None,
        basic_auth_encoded: Optional[str] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = 30.0,
        session: Optional[requests.Session] = None,
        expected_status_code: int = 200,
        validate_response: bool = False,
        log_response: bool = True,
        content_type: str = "application/json",
        **kwargs,
    ):
        self.host = host.rstrip("/") if host else None
        self.method = method.upper()
        self.endpoint = endpoint
        self.json = json
        self.data = data
        self.params = params
        self.bearer_token = bearer_token
        self.basic_auth_encoded = basic_auth_encoded
        self.headers = headers or {}
        self.timeout = timeout
        self.session = session if session is not None else requests.Session()
        self.expected_status_code = expected_status_code
        self.validate_response = validate_response
        self.log_response = log_response
        self.content_type = content_type
        self.verify = kwargs.pop("verify", False)
        self.request_kwargs = kwargs

        valid_methods = ["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS"]
        if self.method not in valid_methods:
            log.error(f"Invalid HTTP method: {self.method}. Must be one of {valid_methods}")
            raise ValueError

    def _build_url(self) -> str:
        return f"{self.host if self.host else ''}{self.endpoint}"

    def _build_headers(self) -> Dict[str, str]:
        headers = self.headers.copy()
        if self.bearer_token:
            headers["Authorization"] = f"Bearer {self.bearer_token}"
        if self.basic_auth_encoded:
            headers["Authorization"] = f"Basic {self.basic_auth_encoded}"
        headers["Content-Type"] = self.content_type
        return headers

    def _mask_sensitive_headers(self, headers: Dict[str, str]) -> Dict[str, str]:
        masked_headers = headers.copy()
        sensitive_keys = ["authorization", "Authorization", "auth", "Auth"]
        for key in sensitive_keys:
            if key in masked_headers:
                value = masked_headers[key]
                if len(value) > 10:
                    masked_headers[key] = f"{value[:10]}...***MASKED***"
                else:
                    masked_headers[key] = "***MASKED***"
        return masked_headers

    def _log_request(self, url: str, headers: Dict[str, str]) -> None:
        request_message = f"""Sending request
        Method: {self.method}
        URL: {url}
        Headers: {self._mask_sensitive_headers(headers)}"""
        if self.params:
            filtered_params = {k: v for k, v in self.params.items() if v is not None}
            if filtered_params:
                request_message += f"\nQuery Params: {filtered_params}"
            else:
                request_message += "\nQuery Params: None"
        if self.json is not None:
            request_message += f"\nJSON Payload: {self.json}"
        if self.data is not None:
            request_message += f"\nForm Data: {self.data}"
        if self.validate_response:
            request_message += f"\nExpected Status Code: {self.expected_status_code}"
        if self.request_kwargs:
            request_message += f"\nAdditional Request Args: {self.request_kwargs}"
        log.debug(request_message)

    def _log_response(self, response: Response) -> None:
        response_message = f"""Received response
        Status Code: {response.status_code}
        Headers: {dict(response.headers)}
        """
        try:
            response_json = response.json()
            if self.log_response:
                response_message += f"Response Body (JSON): {response_json}"
            log.debug(response_message)
        except ValueError:
            response_text = response.text
            if len(response_text) > 1000:
                response_text = response_text[:1000] + "...[TRUNCATED]"
            if self.log_response:
                response_message += f"Response Body (Text): {response_text}"
            log.debug(response_message)

    def _validate_response_status(self, response: Response) -> None:
        if not self.validate_response:
            return
        if response.status_code != self.expected_status_code:
            error_msg = f"Response status code {response.status_code} does not match expected {self.expected_status_code}"
            log.exception(error_msg)
            try:
                response_body = (
                    response.json()
                    if response.headers.get("content-type", "").startswith(
                        "application/json"
                    )
                    else response.text
                )
                log.error(f"Response body: {response_body}")
            except Exception:
                log.error(f"Response text: {response.text}")
            raise requests.exceptions.RequestException(
                f"{error_msg}. URL: {response.url}, Response: {response.text[:200]}{'...' if len(response.text) > 200 else ''}"
            )

    def execute(self) -> Response:
        url = self._build_url()
        headers = self._build_headers()
        self._log_request(url, headers)
        try:
            request_kwargs = {
                "method": self.method,
                "url": url,
                "headers": headers,
                "timeout": self.timeout,
                **self.request_kwargs,
            }
            if self.params:
                filtered_params = {
                    k: v for k, v in self.params.items() if v is not None
                }
                if filtered_params:
                    request_kwargs["params"] = filtered_params
            if self.json is not None:
                request_kwargs["json"] = self.json
            if self.data is not None:
                request_kwargs["data"] = self.data
            response = self.session.request(verify=self.verify, **request_kwargs)
            self._validate_response_status(response)
            self._log_response(response)

            return response
        except requests.exceptions.Timeout:
            log.exception(f"Request timed out after {self.timeout}s")
            raise
        except requests.exceptions.ConnectionError:
            log.exception("Connection error occurred")
            raise
        except requests.exceptions.RequestException:
            log.exception("Request failed")
            raise
        except Exception:
            log.exception("Unexpected error during request execution")
            raise
