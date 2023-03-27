from selenium.webdriver.common.by import By


class OtpPage:
    editNumber = (By.XPATH, "//img[@alt='pen icon']")
    displayNumber = (By.XPATH, "//div[@class='text-[14px] font-normal font-[rubik] text-center']")
    verify = (By.XPATH, "//button[contains(.,'Verify')]")

    def __init__(self, driver):
        self.driver = driver

    def editNum(self):
        return self.driver.find_element(*OtpPage.editNumber)

    def dispNumber(self):
        return self.driver.find_element(*OtpPage.displayNumber)

    def verifyBut(self):
        return self.driver.find_element(*OtpPage.verify)
