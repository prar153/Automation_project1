from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from FinalAutomation_Project.pages.login_page import LoginPage
from FinalAutomation_Project.pages.producthomepage import ProducthomePage


class Testproducthomepage:

    def testproducthomepage(self):

        # OPEN BROWSER
        self.driver = webdriver.Chrome()

        # OPEN WEBSITE
        self.driver.get("https://automationexercise.com/")
        self.driver.maximize_window()

        self.LP = LoginPage(self.driver)
        self.PH = ProducthomePage(self.driver)

        # LOGIN
        self.LP.clickSignuploginurl()

        self.LP.setEmail("manandharpuja@gmail.com")
        self.LP.setPassword("@Shrestha24")

        self.LP.clickSignupbtn()

        # SELECT CATEGORY
        self.PH.selectCategory("Women", "Dress")

        # SELECT BRAND
        self.PH.selectBrand("Polo")

        # ADD PRODUCT
        self.PH.selectAddtocart("Blue Top")

        # CONTINUE SHOPPING
        self.PH.continueShopping()

        # GO TO CART
        self.PH.gotoCart()