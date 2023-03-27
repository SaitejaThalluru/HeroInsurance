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
from pageObject.buyjourney1 import BuyJourney


# from selenium.webdriver.common.action_chains import ActionChains


@pytest.mark.usefixtures("setup")
class Test_BuyJourneyOne:
    # @pytest.mark.skip
    def test_linkValidations(self):
        buy_journey_one = BuyJourney(self.driver)
        print(buy_journey_one.CarNumberField().is_displayed())
        print(buy_journey_one.ViewQuotes().is_displayed())
        print(buy_journey_one.ViewQuotes().is_enabled())
        buy_journey_one.WithoutCarNumberLink().click()
        time.sleep(3)
        if buy_journey_one.WithoutCarPopup().is_displayed():
            print("without car number link is working fine")
            buy_journey_one.BackButton().click()
        else:
            print("without car number link is not working")
        print(buy_journey_one.ViewQuotes().is_displayed)
        buy_journey_one.ClickHere().click()
        time.sleep(3)
        if buy_journey_one.WithoutCarPopup().is_displayed():
            print("click here link is working fine")
            buy_journey_one.BackButton().click()
        else:
            print("click here link is not working")
