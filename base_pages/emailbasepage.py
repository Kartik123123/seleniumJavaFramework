from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class mailbaseclass:


    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def sendkeys(self,locator, text):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        ).clear()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)).send_keys(text)




