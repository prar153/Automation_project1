from selenium import webdriver

from FinalAutomation_Project.pages.login_page import LoginPage


class TestLoginPage:
    def testloginpage(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://automationexercise.com/")
        self.driver.maximize_window()
        self.LP=LoginPage(self.driver)
        self.LP.clickSignuploginurl()
        self.LP.setEmail("manandharpuja@gmail.com")
        self.LP.setPassword("@Shrestha24")
        self.LP.clickSignupbtn()
