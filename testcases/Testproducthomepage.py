from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from FinalAutomation_Project.pages.login_page import LoginPage
from FinalAutomation_Project.pages.producthomepage import ProducthomePage


class Testproducthomepage:

    def testproducthomepage(self):

        # CHROME OPTIONS
        options = Options()

        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument("--incognito")

        prefs = {
            "profile.default_content_setting_values.notifications": 2
        }

        options.add_experimental_option("prefs", prefs)

        # OPEN BROWSER
        self.driver = webdriver.Chrome(options=options)

        # OPEN WEBSITE
        self.driver.get("https://automationexercise.com/")
        self.driver.maximize_window()

        self.driver.execute_script("""
            let ads = document.querySelectorAll('iframe');
            ads.forEach(ad => ad.remove());
        """)

        self.LP = LoginPage(self.driver)
        self.PH = ProducthomePage(self.driver)

        # LOGIN
        self.LP.clickSignuploginurl()

        self.LP.setEmail("manandharpuja@gmail.com")
        self.LP.setPassword("@Shrestha24")

        self.LP.clickSignupbtn()

        # REMOVE ADS AGAIN AFTER LOGIN
        self.driver.execute_script("""
            let ads = document.querySelectorAll('iframe');
            ads.forEach(ad => ad.remove());
        """)

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