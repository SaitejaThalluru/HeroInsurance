import time
import pytest
from selenium import webdriver
# from selenium.webdriver.chromium import options
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pageObject.RegisterJourney import LandingPage
from pageObject.OtpPage import OtpPage


@pytest.mark.usefixtures("setup")
class TestLandingPage:
    # @pytest.mark.smoke
    def test_logoVerification(self):

        logo = self.driver.find_element(By.XPATH, "//img[@alt='logo']")
        print(logo.is_displayed())
        current_logo_value = logo.get_attribute("value")
        print(current_logo_value)
        support_mail = self.driver.find_element(By.XPATH, "//div[contains(text(),'support@heroibl.com')]")
        assert "support@heroibl.com" in support_mail.text
        print(support_mail.text)

    # @pytest.mark.smoke
    def test_chatIconVerification(self):
        chat_support = self.driver.find_element(By.XPATH, "//img[contains(@alt,'user assistance')]")
        chat_support.click()
        question_1 = self.driver.find_element(By.XPATH, "//p[contains(text(),'Hello! How we can assist you?')]")
        print(question_1.is_displayed())
        print(question_1.text)
        questions = self.driver.find_elements(By.XPATH, "//button[@class='bg-blue']")
        for question in questions:

            question.click()
            if question.text == "call now":
                assert "18001024376" in self.driver.find_element(By.XPATH, "//p[contains(text(),'1800 102 4376')]".text)
            if question.text == "send mail":
                assert "support@heroibl.com" in self.driver.find_element(By.XPATH,
                                                                         "//p[contains(text(),'support@heroibl.com')]".text)
            if question.text == "Request Call Back":
                submit = self.driver.find_element(By.XPATH, "//button[contains(text(),'Sumbit')]")
                print(submit.is_enabled())
                self.driver.find_element(By.XPATH, "//input[@maxlength='40']").send_keys("Teja")
                self.driver.find_element(By.XPATH,
                                         "//body[1]/div[1]/div[1]/div[1]/div[9]/div[1]/div[2]/div[3]/div[1]/form[1]/div[1]/div[2]/div[1]/div[1]/input[1]").send_keys(
                    "9897879787")
                self.driver.find_element(By.XPATH, "//textarea[@maxlength='200']").send_keys("NEW QUERY")
                print(submit.is_enabled())
                submit.click()
                # notification = self.driver.find_element(By.XPATH, ".ant-notification-notice-message")
                # print(notification.is_displayed())

    # @pytest.mark.skip
    def test_register(self):
        landing_page = LandingPage(self.driver)
        otp_page = OtpPage(self.driver)
        landing_page.registerBut().click()
        print(landing_page.registerName().is_displayed())
        landing_page.registerName().send_keys('Test')
        # time.sleep(2)
        try:
            if landing_page.NameError().is_displayed():
                print("Invalid Name")
                self.driver.close()

        except:
            pass
        landing_page.registerEmail().send_keys('Testing8@gmail.com')
        try:
            if landing_page.EmailError().is_displayed():
                print('Invalid Email')
                self.driver.close()
        except:
            pass
        time.sleep(3)
        number = self.driver.find_element(By.CSS_SELECTOR, "form div:nth-child(3) input")
        number.send_keys("8919396555")
        try:
            if landing_page.NumberError().is_displayed():
                print("Invalid Number")
                self.driver.close()
        except:
            pass
        landing_page.continueRegister().click()
        time.sleep(3)
        try:
            if landing_page.Success().is_displayed():
                print("Registration started for new user")
        except:
            print("Registration Failed ")
            self.driver.close()
        landing_page.Ok().click()
        self.driver.get_screenshot_as_file("screenshot.png")
        if landing_page.VerifyOtp().is_displayed():
            print("OTP is sent")
        else:
            print("OTP is not sent")
        time.sleep(10)
        if otp_page.verifyBut().is_displayed() and otp_page.verifyBut().is_enabled():
            otp_page.verifyBut().click()
        else:
            print("not clickable - enter otp")
            self.driver.close()
        time.sleep(1)

        landing_page.PanCard().send_keys("AXZPT8541P")
        try:
            time.sleep(3)
            if landing_page.PanError().is_displayed:
                print("Invalid Pan name")
        except:
            print("Valid Pan")
            landing_page.PanContinue().click()
            time.sleep(1)
        landing_page.PanVerifyOk().click()
        time.sleep(3)
        try:
            if landing_page.PanContinueDetails().is_displayed():
                print("Pan verified")
                landing_page.PanContinueDetails().click()
        except:
            print("pan verification failed")
            self.driver.close()
        continue_details = self.driver.find_element(By.XPATH, "//button[.='Continue']")
        if continue_details.is_enabled() and continue_details.is_displayed():
            print("continue button is enabled")
        else:
            pass

        landing_page.YourName().get_attribute("value")
        current_name = landing_page.YourName().get_attribute("value")
        print(current_name)
        current_email = landing_page.YourEmail().get_attribute("value")
        print(current_email)
        dob = self.driver.find_element(By.XPATH, "//input[@placeholder='dd/mm/yyyy']")
        dob.send_keys("12/05/1998")
        current_fname = landing_page.FatherName().get_attribute("value")
        print(current_fname)
        landing_page.Aadhar().send_keys("455446043913")
        current_pan = landing_page.PanCard().get_attribute("value")
        print(current_pan)
        landing_page.AddressOne().send_keys('Nellore')
        landing_page.AddressTwo().send_keys("vgr")
        landing_page.PinCode().send_keys("524404")
        landing_page.CityName().click()
        landing_page.CityName().send_keys("Nellore")
        time.sleep(3)
        landing_page.EducationQualification().send_keys("Graduate")
        time.sleep(3)
        landing_page.SelectProduct().send_keys("Motor")
        time.sleep(3)
        landing_page.NocAvailable().send_keys("no")
        time.sleep(3)
        if continue_details.is_enabled() and continue_details.is_displayed():
            print("continue button is enabled")
            continue_details.click()
            print("personal details filled")
            time.sleep(5)
        else:
            print("continue is still disabled")
            continue_details.click()
        landing_page.BankName().send_keys("HDFC")
        time.sleep(2)
        landing_page.IfscCode().send_keys("SBIN0125620")
        try:
            ifsc_error = self.driver.find_element(By.XPATH, "//div[.='Please enter valid IFSC code.']")
            if ifsc_error.is_displayed():
                print("Invalid IFSC")
        except:
            pass
        try:
            holder_error = self.driver.find_element(By.XPATH, "//div[.='Please enter valid account holder name.']")
            if holder_error.is_displayed():
                print("Invalid Account holder name")
        except:
            landing_page.HolderName().send_keys("Sai teja")
        try:
            account_error = self.driver.find_element(By.XPATH, "//div[.='Please enter valid account number.']")
            if account_error.is_displayed():
                print("invalid account number")
        except:
            landing_page.AccountNumber().send_keys("40535577549")
        if landing_page.PayOutContinue().is_displayed() and landing_page.PayOutContinue().is_enabled():
            print("Payout details filled")
        time.sleep(3)
