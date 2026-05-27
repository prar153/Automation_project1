from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class LoginPage:
    signuploginbutton_xpath = "//a[normalize-space()='Signup / Login']"
    loginemail_xpath="//input[@data-qa='login-email']"
    password_xpath="//input[@placeholder='Password']"
    loginbtn_xpath="//button[normalize-space()='Login']"


    def __init__(self, driver):
        self.driver = driver

    def clickSignuploginurl(self):
        slurl=self.driver.find_element(By.XPATH,self.signuploginbutton_xpath)
        slurl.click()

    def setEmail(self,email):
        lemail=self.driver.find_element(By.XPATH,self.loginemail_xpath)
        lemail.clear()
        lemail.send_keys(email)

    def setPassword(self,passwd):
        pwd=self.driver.find_element(By.XPATH,self.password_xpath)
        pwd.clear()
        pwd.send_keys(passwd)

    def clickSignupbtn(self):
        loginbtn=self.driver.find_element(By.XPATH,self.loginbtn_xpath)
        loginbtn.click()

