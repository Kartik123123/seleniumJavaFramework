from base_pages.emailbasepage import mailbaseclass
from selenium.webdriver.common.by import By

class yopmailpage(mailbaseclass):
    textbox = (By.ID, "login")
    arrow = (By.XPATH, "//button[@class='md']/i")


    def mailboxopen (self, mail):
        self.sendkeys(self.textbox,mail)
        self.click(self.arrow)


