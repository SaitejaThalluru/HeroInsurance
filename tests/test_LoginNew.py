import time
import pytest
from selenium import webdriver
# from selenium.webdriver import Keys
# from selenium.webdriver.chromium import options
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObject.RegisterJourney import LandingPage
from pageObject.OtpPage import OtpPage


# from selenium.webdriver.common.action_chains import ActionChains


@pytest.mark.usefixtures("setup")
class TestLoginFlow:
    # @pytest.mark.skip
    def test_loginNumber(self):
        landing_page_login = LandingPage(self.driver)
        otp_page = OtpPage(self.driver)
        landing_page_login.loginNum().send_keys("8919396555")
        try:
            if landing_page_login.LoginNumberError().is_displayed():
                print("Invalid Number")
                self.driver.close()

        except:
            pass
        landing_page_login.contButton().click()
        try:
            if otp_page.editNum().is_displayed():
                print("Existing user")

        except:
            print("user doesn't exist- register first/Enter again after 3 minutes")
            self.driver.close()

        # otp_page.editNum().click()
        # landing_page_login.loginNum().send_keys(
        # Keys.BACKSPACE * len(landing_page_login.loginNum().get_attribute("value")))
        # landing_page_login.loginNum().send_keys("8919396555")
        # landing_page_login.contButton().click()
        time.sleep(20)
        if otp_page.verifyBut().is_enabled() and otp_page.verifyBut().is_displayed():
            otp_page.verifyBut().click()
            time.sleep(3)
        else:
            print("not clickable - enter otp")
            self.driver.close()

        try:
            # if otp_page.verifyBut().is_enabled() and otp_page.verifyBut().is_displayed():
            # otp_page.verifyBut().click()
            wrong_otp = self.driver.find_element(By.XPATH, "//p[contains(text(),'Wrong OTP')]")
            if wrong_otp.is_displayed():
                print("wrong otp")
            if not wrong_otp.is_displayed():
                print("Valid otp")

        except:
            # if otp_page.verifyBut().is_enabled() and otp_page.verifyBut().is_displayed():
            # otp_page.verifyBut().click()
            pass
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//img[@alt='User_Photo']")))
        dashboard_image = self.driver.find_element(By.XPATH, "//img[@alt='User_Photo']")
        if dashboard_image.is_displayed():
            print("Login successful to dashboard")

    def test_MyAccount(self):
        landing_page_login = LandingPage(self.driver)
        otp_page = OtpPage(self.driver)
        landing_page_login.loginNum().send_keys("8919396555")
        landing_page_login.contButton().click()
        time.sleep(20)
        otp_page.verifyBut().click()
        my_account = self.driver.find_element(By.XPATH, "//span[@class='ant-avatar ant-avatar-circle']")
        my_account.click()
        wait = WebDriverWait(self.driver, 20)
        wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//div[contains(text(),'testings@gmail.com')]")))
        current_email = self.driver.find_element(By.XPATH, "//div[contains(text(),'testings@gmail.com')]")
        current_email_text = current_email.text
        print(current_email_text)
        change_email_link = self.driver.find_element(By.XPATH, "//img[@class='h-[18px] pl-[10px]']")
        self.driver.back()
        time.sleep(2)
