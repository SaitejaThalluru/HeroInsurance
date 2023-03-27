from selenium.webdriver.common.by import By


class LandingPage:
    login_number = (By.TAG_NAME, "input")
    login_number_error = (By.XPATH, "//div[.='Please enter valid mobile number.']")
    conti_button = (By.XPATH, "//button[@tabindex='0']")
    register_button = (By.XPATH, "//div[contains(text(),'Register')]")
    register_name = (By.XPATH, "//input[@maxlength='40']")
    register_email = (By.XPATH, "(//input[@maxlength='40'])[2]")
    conti_register = (By.XPATH, "//div[@class='my-4']")
    name_error = (By.XPATH, "//div[.='Please enter valid name.']")
    email_error = (By.XPATH, "//div[.='Please enter valid E-mail.']")
    num_error = (By.XPATH, "//div[.='Please enter valid mobile number.']")
    success = (By.XPATH, "//div[.='Email & OTP Authentication']")
    ok = (By.XPATH, "//div[contains(@class,'my-4 w-[100px] h-[42px] rounded-[23px] bg-[#E72026] cursor-pointer')]")
    verify_otp = (By.XPATH, "//div[.='Verify OTP']")
    Pan_card = (By.TAG_NAME, "input")
    Pan_continue = (By.XPATH, "//div[.='Continue']")
    pan_error = (By.XPATH, "//div[.='Please enter valid PAN details.']")
    pan_verify_ok = (
    By.XPATH, "//div[contains(@class,'w-[270px] h-[42px] mt-4 rounded-[23px] bg-[#E72026] cursor-pointer')]")
    pan_continue_details = (By.XPATH, "//div[contains(text(),'Continue to Fill Personal Details')]")
    your_name = (By.XPATH, "(//input[@id='outlined'])[1]")
    your_email = (By.XPATH, "(//input[@id='outlined'])[1]")
    dob = (By.XPATH, "(//input[@placeholder='dd/mm/yyyy']")
    father_name = (By.XPATH, "(//input[@id='outlined'])[3]")
    aadhar = (By.XPATH, "//input[@maxlength='12']")
    pan_cardnum = (By.XPATH, "//input[@id='outlined-required'])[2]")
    address_one = (By.XPATH, "(//input[@maxlength='100'])[1]")
    address_two = (By.XPATH, "(//input[contains(@maxlength,'100')])[2]")
    pin = (By.XPATH, "//input[@maxlength='6']")
    city_name = (By.XPATH, "(//input[@aria-autocomplete='list'])[2]")
    education_qualification = (By.XPATH, "(//input[@aria-autocomplete='list'])[3]")
    select_product = (By.XPATH, "(//input[@aria-autocomplete='list'])[5]")
    noc_available = (By.XPATH, "(//input[@aria-autocomplete='list'])[6]")
    bank_name = (By.ID, "combo-box-demo")
    ifsc_number = (By.XPATH, "//input[@maxlength='11']")
    holder_name = (By.XPATH, "//input[@maxlength='40']")
    account_number = (By.XPATH, "//input[@maxlength='16']")
    payout_continue = (By.XPATH, "//button[.='Continue']")

    def __init__(self, driver):
        self.driver = driver

    def YourName(self):
        return self.driver.find_element(*LandingPage.your_name)

    def YourEmail(self):
        return self.driver.find_element(*LandingPage.your_email)

    def DOB(self):
        return self.driver.find_element(*LandingPage.dob)

    def FatherName(self):
        return self.driver.find_element(*LandingPage.father_name)

    def Aadhar(self):
        return self.driver.find_element(*LandingPage.aadhar)

    def PanCardNum(self):
        return self.driver.find_element(*LandingPage.pan_cardnum)

    def AddressOne(self):
        return self.driver.find_element(*LandingPage.address_one)

    def AddressTwo(self):
        return self.driver.find_element(*LandingPage.address_two)

    def PinCode(self):
        return self.driver.find_element(*LandingPage.pin)

    def CityName(self):
        return self.driver.find_element(*LandingPage.city_name)

    def EducationQualification(self):
        return self.driver.find_element(*LandingPage.education_qualification)

    def SelectProduct(self):
        return self.driver.find_element(*LandingPage.select_product)

    def NocAvailable(self):
        return self.driver.find_element(*LandingPage.noc_available)

    def BankName(self):
        return self.driver.find_element(*LandingPage.bank_name)

    def IfscCode(self):
        return self.driver.find_element(*LandingPage.ifsc_number)

    def HolderName(self):
        return self.driver.find_element(*LandingPage.holder_name)

    def AccountNumber(self):
        return self.driver.find_element(*LandingPage.account_number)

    def PayOutContinue(self):
        return self.driver.find_element(*LandingPage.payout_continue)

    def loginNum(self):
        return self.driver.find_element(*LandingPage.login_number)

    def contButton(self):
        return self.driver.find_element(*LandingPage.conti_button)

    def registerBut(self):
        return self.driver.find_element(*LandingPage.register_button)

    def registerName(self):
        return self.driver.find_element(*LandingPage.register_name)

    def registerEmail(self):
        return self.driver.find_element(*LandingPage.register_email)

    def continueRegister(self):
        return self.driver.find_element(*LandingPage.conti_register)

    def NameError(self):
        return self.driver.find_element(*LandingPage.name_error)

    def EmailError(self):
        return self.driver.find_element(*LandingPage.email_error)

    def NumberError(self):
        return self.driver.find_element(*LandingPage.num_error)

    def Success(self):
        return self.driver.find_element(*LandingPage.success)

    def Ok(self):
        return self.driver.find_element(*LandingPage.ok)

    def VerifyOtp(self):
        return self.driver.find_element(*LandingPage.verify_otp)

    def PanCard(self):
        return self.driver.find_element(*LandingPage.Pan_card)

    def PanContinue(self):
        return self.driver.find_element(*LandingPage.Pan_continue)

    def PanError(self):
        return self.driver.find_element(*LandingPage.pan_error)

    def PanVerifyOk(self):
        return self.driver.find_element(*LandingPage.pan_verify_ok)

    def PanContinueDetails(self):
        return self.driver.find_element(*LandingPage.pan_continue_details)

    def LoginNumberError(self):
        return self.driver.find_element(*LandingPage.login_number_error)
