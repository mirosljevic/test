from playwright.sync_api import Page, Browser, BrowserContext
from typing import Optional
from functools import cached_property
from requests import Session

from models.player import Player
from logger import log
from environment import hosts, credentials
from settings.devices import get_current_device_config
from .features import PlayerRegistrationUi, PlayerAuthenticationUi, PlayerInstantsUi, \
    PlayerAccountUi, PlayerPaymentsUi, PlayerBonusUi, PlayerDrawGamesUi, PlayerDocumentsUi, PlayerClaimsUi


class PlayerFacade:
    def __init__(self, player: Optional[Player] = None, browser: Optional[Browser] = None,
                 session: Session = None):
        self.player = player
        self.browser = browser
        self.context = None
        self.page = None
        self.session = session

    @property
    def registration(self):
        return PlayerRegistrationUi(self.page, self.player)

    @property
    def authentication(self):
        return PlayerAuthenticationUi(self.page, self.player)

    @property
    def account(self):
        return PlayerAccountUi(self.page, self.player)

    @property
    def dgs(self):
        return PlayerDrawGamesUi(self.page, self.player)

    @property
    def instants(self):
        return PlayerInstantsUi(self.page, self.player)

    @property
    def payments(self):
        return PlayerPaymentsUi(self.page, self.player)

    @property
    def bonus(self):
        return PlayerBonusUi(self.page, self.player)

    @property
    def documents(self):
        return PlayerDocumentsUi(self.page, self.player)

    @property
    def claims(self):
        return PlayerClaimsUi(self.page, self.player)
    
    @property
    def is_mobile(self) -> bool:
        if self.context:
            return getattr(self.context, '_is_mobile', False)
        else:
            device_config = get_current_device_config()
            return device_config.get('is_mobile', False)

    def open(self, device_name: str = None, **kwargs):
        if device_name:
            kwargs['device_name'] = device_name
            from settings.devices import get_device_config
            device_config = get_device_config(device_name)
            for key, value in device_config.items():
                if key not in kwargs:
                    kwargs[key] = value
        
        if not self.context:
            self.context = self._create_context(**kwargs)
        
        if not self.page:
            page = self.context.new_page()
            self.page = page
            self.page.goto(hosts.gameweb)
            log.debug(f"New page opened for and navigated to: {hosts.gameweb}")
        else:
            self.page.goto(hosts.gameweb)
            log.debug(f"Existing page navigated to: {hosts.gameweb}")

    def _create_context(self, **kwargs) -> BrowserContext:
        context = self.context
        if not context:
            device_config = get_current_device_config()
            
            if 'record_video_dir' not in kwargs:
                kwargs['record_video_dir'] = "test-results/videos"
            if 'record_video_size' not in kwargs:
                kwargs['record_video_size'] = device_config.get('record_video_size', {"width": 1280, "height": 720})
            
            context_options = {
                "locale": "en-US",
                "timezone_id": "America/New_York",
                "http_credentials": credentials.http_credentials,
                "ignore_https_errors": True,
                "permissions": ["geolocation"],
                "geolocation": {"latitude": self.player.latitude if self.player else None,
                                "longitude": self.player.longitude if self.player else None},
                "storage_state": self._get_cookies(),
                "viewport": device_config.get('viewport'),
                "user_agent": device_config.get('user_agent'),
                "device_scale_factor": device_config.get('device_scale_factor'),
                "is_mobile": device_config.get('is_mobile'),
                "has_touch": device_config.get('has_touch'),
                **kwargs
            }
            
            context_options = {k: v for k, v in context_options.items() if v is not None}
            context = self.browser.new_context(**context_options)
            context._is_mobile = device_config.get('is_mobile', False)
            device_name = kwargs.get('device_name', 'current device')
            log.debug(f"New browser context created with device configuration: {device_name}")
            log.debug(f"Viewport: {device_config.get('viewport')}, Mobile: {device_config.get('is_mobile')}")
            
        return context

    def close(self):
        if self.page:
            self.page.close()
            log.debug("Page closed.")
            self.page = None

        if self.context:
            self.context.close()
            log.debug("Browser context closed.")
            self.context = None

    def _get_cookies(self):
        if self.session:
            cookies = self.session.cookies
            pw_cookies = []

            for cookie in cookies:
                pw_cookie = {
                    "name": cookie.name,
                    "value": cookie.value,
                    "domain": cookie.domain,
                    "path": cookie.path or "/",
                    "expires": -1 if cookie.expires is None else cookie.expires,
                    "httpOnly": False,
                    "secure": cookie.secure,
                    "sameSite": "Lax"
                }
                pw_cookies.append(pw_cookie)

            return {
                "cookies": pw_cookies,
                "origins": []
            }
        return None

