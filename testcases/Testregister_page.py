from selenium import webdriver

from FinalAutomation_Project.pages.register_page import RegisterPage


class Testregisterpage:
    def test_registerpage(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://automationexercise.com/")
        self.driver.maximize_window()
        self.LP=RegisterPage(self.driver)
        self.LP.clicksignuploginurl()
        self.LP.setName('Puj Manandhar')
        self.LP.setEmail('manandharpuj@gmail.com')
        self.LP.clickSignupbtn()
        self.LP.setTitle()
        self.LP.setPassword('@Shrestha24')
        self.LP.setDateDay(4)
        self.LP.setDateMonth("May")
        self.LP.setDateYear("2018")
        self.LP.setFirstname("Puja")
        self.LP.setLastname("Manandhar")
        self.LP.setCompany("LG Company")
        self.LP.setAddress("Checkpost")
        self.LP.setCountry("New Zealand")
        self.LP.setState('Bagmati')
        self.LP.setCity('Kathmandu')
        self.LP.setZipcode('44600')
        self.LP.setMobileNumber('98765445678')
        self.LP.clickCreateAcctBtn()