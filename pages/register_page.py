from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class RegisterPage:
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
    createaccbtn_xpath="//button[normalize-space()='Create Account']"

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

    def setDateDay(self,day):
        dateday=self.driver.find_element(By.XPATH,self.dateday_xpath)
        options=Select(dateday)
        options.select_by_index(day)

    def setDateMonth(self,datemth):
        datemonth=self.driver.find_element(By.XPATH,self.datemonth_xpath)
        options=Select(datemonth)
        options.select_by_visible_text(datemth)

    def setDateYear(self,dateyr):
        dateyear=self.driver.find_element(By.XPATH,self.dateyear_xpath)
        options=Select(dateyear)
        options.select_by_visible_text(dateyr)

    def setFirstname(self,fname):
        firstname=self.driver.find_element(By.XPATH,self.firstname_xpath)
        firstname.clear()
        firstname.send_keys(fname)

    def setLastname(self,lname):
        lastname=self.driver.find_element(By.XPATH,self.lastname_xpath)
        lastname.clear()
        lastname.send_keys(lname)

    def setCompany(self,comp):
        company=self.driver.find_element(By.XPATH,self.company_xpath)
        company.clear()
        company.send_keys(comp)

    def setAddress(self,add):
        address=self.driver.find_element(By.XPATH,self.address_xpath)
        address.clear()
        address.send_keys(add)

    def setCountry(self,ctry):
        country=self.driver.find_element(By.XPATH,self.country_xpath)
        coptions=Select(country)
        coptions.select_by_visible_text(ctry)

    def setState(self,stat):
        state=self.driver.find_element(By.XPATH,self.state_xpath)
        state.clear()
        state.send_keys(stat)
    def setCity(self,ct):
        city=self.driver.find_element(By.XPATH,self.city_xpath)
        city.clear()
        city.send_keys(ct)

    def setZipcode(self,zip):
        zp=self.driver.find_element(By.XPATH,self.zipcode_xpath)
        zp.clear()
        zp.send_keys(zip)

    def setMobileNumber(self,num):
        sm=self.driver.find_element(By.XPATH,self.mobilenumber_xpath)
        sm.clear()
        sm.send_keys(num)

    def clickCreateAcctBtn(self):
        createbtn=self.driver.find_element(By.XPATH,self.createaccbtn_xpath)
        createbtn.click()

