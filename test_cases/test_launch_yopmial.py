from test_cases.conftest import setup
from base_pages.yopmail import yopmailpage

class Testlaunchyopmail:

    mail = "test@yopmail.com"
    def test_open_mailbox(self, setup):
        self.driver = setup
        self.driver.get("https://yopmail.com/en/")
        self.obj = yopmailpage(self.driver)
        self.obj.mailboxopen(self.mail)

