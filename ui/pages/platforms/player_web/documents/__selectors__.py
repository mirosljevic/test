from ui.pages.locator import Selectors


class UploadDocumentsSelectors:
    tab_button = Selectors(default="[role='tab']")
    add_file_input = Selectors(data_test_id="pc-file-input")
    continue_button = Selectors(data_test_id="pc-upload-button")
