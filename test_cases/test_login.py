import time

import pytest
from selenium import webdriver

from base_pages.LOGIN_page import Login_pages
from test_cases.conftest import setup
from utilities.login_otp import get_otp

class Testlogin:

    url = "https://retail-dev.vinecrms.com/"
    Email="kartikc@regenesys.net"

    def test_close_valid(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.loggin = Login_pages(self.driver)
        self.loggin.close_moddle()
        self.loggin.enter_username(self.Email)
        self.loggin.click_send_button()
        self.loggin.close_moddle()
        self.otp = get_otp(self.Email)
        self.loggin.otp_submit(self.otp)
        self.loggin.submit_login()
        self.loggin.lead_click()

    def logged_in(self, setup):
        self.driver = setup
        self.loggin = Login_pages(self.driver)
        self.driver.get(self.url)












