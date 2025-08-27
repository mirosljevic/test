from logger import log


class Selectors:
    def __init__(self,
                 default=None,
                 mobile=None,
                 kansas=None,
                 kansas_mobile=None,
                 data_test_id=None,
                 data_test_mobile_id=None
                 ):
        self.default = default
        self.mobile = mobile or default
        self.kansas = kansas or default
        self.kansas_mobile = kansas_mobile or mobile or kansas or default
        self.data_test_id = data_test_id
        self.data_test_mobile_id = data_test_mobile_id or data_test_id

    def get_selector(self, layout: str, tenant: str = "default") -> str:
        if self.get_data_test_selector(layout):
            return self.get_data_test_selector(layout)

        if tenant == "default":
            if layout == "desktop":
                return self.default
            elif layout == "tablet":
                return self.mobile
            elif layout == "mobile":
                return self.mobile
        elif tenant == "kansas":
            if layout == "desktop":
                return self.kansas
            elif layout == "tablet":
                return self.kansas_mobile
            elif layout == "mobile":
                return self.kansas_mobile
        else:
            log.error(f"Unknown tenant: {tenant}. Using default selector.")
            return self.default

    def get_data_test_selector(self, layout: str) -> str:
        template = "//*[@data-test-id='{}']"
        if layout in ["mobile", "tablet"]:
            return template.format(self.data_test_mobile_id) if self.data_test_mobile_id else None
        else:
            return template.format(self.data_test_id) if self.data_test_id else None

