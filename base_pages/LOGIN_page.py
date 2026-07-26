import email
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Login_pages:
    close_moddle_id = "close-modal"
    Email_sender_id = "email"
    otp_send_button_xpath = "//div[@id='login-otp']/strong"
    otp_submit_button_id = "password"
    Login_clicked_id = "login-submit"
    lead_id = "//a[contains(text(), 'Kartik Chourasiya')]"


    def __init__(self, driver):
        self.driver = driver

    def close_moddle(self):
        WebDriverWait(self.driver ,10).until(
            EC.element_to_be_clickable((By.ID,self.close_moddle_id))
            ).click()

    def enter_username(self, mail):
        self.driver.find_element(By.ID, self.Email_sender_id).send_keys(mail)

    def click_send_button(self):
        self.driver.find_element(By.XPATH, self.otp_send_button_xpath).click()

    def otp_submit(self, otp):
       self.driver.find_element(By.ID, self.otp_submit_button_id).send_keys(otp)

    def submit_login(self):
        self.driver.find_element(By.ID, self.Login_clicked_id).click()

    def check_login_status(self):
        actual_text = self.driver.find_element(By.XPATH, "//h3[contains(text(), 'Dashboard')]").text()

    def lead_click(self):
        self.driver.find.element(By.XPATH, "//a[contains(text(), 'Kartik Chourasiya'')]").click()









