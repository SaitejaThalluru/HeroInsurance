import pytest
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pageObject.OtpPage import OtpPage
from pageObject.RegisterJourney import LandingPage


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        serv_obj = Service(r"C:\Users\ThalluruSaiteja\Downloads\chromedriver_win32/chromedriver.exe")
        driver = webdriver.Chrome(service=serv_obj)
        driver.implicitly_wait(2)
        driver.maximize_window()
        driver.get("http://202.56.238.216/#/")
        # driver.get("http://202.56.238.216/#/buy-journey")
        # wait = WebDriverWait(driver, 10)
        # wait.until(expected_conditions.visibility_of_element_located(By.XPATH, "//img[@alt='logo']"))
        request.cls.driver = driver
        yield
        driver.close()
    elif browser_name == "firefox":
        # serv_obj = Service(r"C:\Users\ThalluruSaiteja\Downloads\geckodriver-v0.32.2-win32\geckodriver.exe")
        # driver = webdriver.Firefox(service=serv_obj)
        options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        driver = webdriver.Firefox(
            executable_path=r'C:\Users\ThalluruSaiteja\Downloads\geckodriver-v0.32.2-win32\geckodriver.exe',
            options=options)

        driver.implicitly_wait(2)
        driver.maximize_window()
        driver.get("http://202.56.238.216/#/")
        # driver.get("http://202.56.238.216/#/buy-journey")
        request.cls.driver = driver
        yield
        driver.close()


