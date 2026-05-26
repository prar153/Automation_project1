from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class LoginPage:
    signuploginbutton_xpath="//a[normalize-space()='Signup / Login']"
    signupname_xpath="//input[@placeholder='Name']"
    signupemail_xpath="//input[@data-qa='signup-email']"
    signupbtn_xpath="//button[normalize-space()='Signup']"

    title_xpath="//input[@id='id_gender2']"

    password_xpath="//input[@id='password']"
    dateday_xpath="//select[@id='days']"
    datemonth_xpath="//select[@id='months']"
    dateyear_xpath="//select[@id='years']"
    firstname_xpath="//input[@id='first_name']"
    lastname_xpath="//input[@id='last_name']"
    company_xpath="//input[@id='company']"
    address_xpath="//input[@id='address1']"
    country_xpath="//select[@id='country']"
    state_xpath="//input[@id='state']"
    city_xpath="//input[@id='city']"
    zipcode_xpath="//input[@id='zipcode']"
    mobilenumber_xpath="//input[@id='mobile_number']"
    createaccbtn_xpath="//input[@id='mobile_number']"

    def __init__(self, driver):
        self.driver = driver

    def clicksignuploginurl(self):
        signuplgnurl=self.driver.find_element(By.XPATH,self.signuploginbutton_xpath)
        signuplgnurl.click()

    def setName(self,name):
        sname=self.driver.find_element(By.XPATH,self.signupname_xpath)
        sname.clear()
        sname.send_keys(name)

    def setEmail(self,email):
        semail=self.driver.find_element(By.XPATH,self.signupemail_xpath)
        semail.clear()
        semail.send_keys(email)

    def clickSignupbtn(self):
        signupbtn=self.driver.find_element(By.XPATH,self.signupbtn_xpath)
        signupbtn.click()

    def setTitle(self):
        stitle=self.driver.find_element(By.XPATH,self.title_xpath)
        stitle.click()

    def setPassword(self,passwd):
        pwd=self.driver.find_element(By.XPATH,self.password_xpath)
        pwd.clear()
        pwd.send_keys(passwd)

    def setDateDay(self,dateday):
        dateday=self.driver.find_element(By.XPATH,self.dateday_xpath)
        dateday.click()
        options=Select(dateday)
        options.select_by_visible_text(4)
