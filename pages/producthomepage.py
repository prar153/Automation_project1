from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProducthomePage():

    Continuebtn_xpath = "//button[normalize-space()='Continue Shopping']"
    Cartlink_xpath = "//a[normalize-space()='Cart']"

    def __init__(self, driver):
        self.driver = driver

    def selectCategory(self, ctg, clothes):
        category = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//a[normalize-space()='{ctg}']")
            )
        )

        self.driver.execute_script("arguments[0].click();", category)

        # CLICK SUB CATEGORY
        furthercategory = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//div[@id='Women']//a[contains(text(),'{clothes}')]")
            )
        )

        self.driver.execute_script("arguments[0].click();", furthercategory)

    def selectBrand(self, br):

        brand = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//a[@href='/brand_products/{br}']")
            )
        )

        self.driver.execute_script("arguments[0].click();", brand)

    def selectAddtocart(self, idn):

        addbtn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//p[text()='{idn}']/following::a[@data-product-id][1]")
            )
        )

        self.driver.execute_script("arguments[0].click();", addbtn)

    def continueShopping(self):

        continuebtn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.Continuebtn_xpath)
            )
        )

        self.driver.execute_script("arguments[0].click();", continuebtn)

    def gotoCart(self):

        cartlink = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.Cartlink_xpath)
            )
        )

        self.driver.execute_script("arguments[0].click();", cartlink)