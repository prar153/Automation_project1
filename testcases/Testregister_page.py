from selenium import webdriver

from FinalAutomation_Project.pages.register_page import RegisterPage


class Testregisterpage:
    def test_registerpage(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://automationexercise.com/")
        self.driver.maximize_window()
        self.RP=RegisterPage(self.driver)
        self.RP.clicksignuploginurl()
        self.RP.setName('Puj Manandhar')
        self.RP.setEmail('manandharpuj@gmail.com')
        self.RP.clickSignupbtn()
        self.RP.setTitle()
        self.RP.setPassword('@Shrestha24')
        self.RP.setDateDay(4)
        self.RP.setDateMonth("May")
        self.RP.setDateYear("2018")
        self.RP.setFirstname("Puja")
        self.RP.setLastname("Manandhar")
        self.RP.setCompany("LG Company")
        self.RP.setAddress("Checkpost")
        self.RP.setCountry("New Zealand")
        self.RP.setState('Bagmati')
        self.RP.setCity('Kathmandu')
        self.RP.setZipcode('44600')
        self.RP.setMobileNumber('98765445678')
        self.RP.clickCreateAcctBtn()