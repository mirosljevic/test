from ui.pages.platforms.player_web.home import HomePage
from ui.pages.platforms.player_web.account import MyAccountPage
from ui.pages.platforms.player_web.documents import UploadDocumentsPage


class PlayerDocumentsUi:
    def __init__(self, page, player=None):
        self.page = page
        self.player = player

        self.home_page = HomePage(page=page)
        self.my_account_page = MyAccountPage(page=page)
        self.upload_documents_page = UploadDocumentsPage(page=page)

    def go_to_upload_documents(self):
        self.home_page.user_controls.user_menu.select("My Account")
        self.my_account_page.my_account_menu.select("Upload Documents")

    def upload(self, document_type: str, file="files/documents/sample.pdf"):
        self.go_to_upload_documents()
        self.upload_documents_page.tab(document_type).click()
        self.upload_documents_page.add_document(file)
        return self

