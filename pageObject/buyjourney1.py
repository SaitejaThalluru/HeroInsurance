from selenium.webdriver.common.by import By


class BuyJourney:
    car_number = (By.XPATH, "//input[@maxlength='20']")
    view_quotes = (By.XPATH, "//button[contains(text(),'View Quotes')]")
    without_car_link = (By.XPATH, "//button[contains(text(),'Proceed With out car number')]")
    back_button = (By.XPATH, "//img[@alt='back']")
    without_car_number_popup = (By.XPATH, "//div[@class='w-full text-center font-bold text-[18px]']")
    click_here = (By.XPATH, "//button[contains(.,'Click here')]")

    def __init__(self, driver):
        self.driver = driver

    def CarNumberField(self):
        return self.driver.find_element(*BuyJourney.car_number)

    def ViewQuotes(self):
        return self.driver.find_element(*BuyJourney.view_quotes)

    def WithoutCarNumberLink(self):
        return self.driver.find_element(*BuyJourney.without_car_link)

    def BackButton(self):
        return self.driver.find_element(*BuyJourney.back_button)

    def WithoutCarPopup(self):
        return self.driver.find_element(*BuyJourney.without_car_number_popup)

    def ClickHere(self):
        return self.driver.find_element(*BuyJourney.click_here)