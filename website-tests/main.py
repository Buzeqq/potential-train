from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from random import choice, sample


WEBSITE = "https://localhost:4433"


class Website(object):
    def __init__(self, driver, element):
        self.driver = driver
        self.element = element
    
    def __enter__(self):
        self.element.click()

    def __exit__(self, *args):
        self.driver.back()


class Customer:
    def __init__(self):
        options = Options()
        options.add_argument('ignore-certificate-errors')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get(WEBSITE)

    def find_category(self):
        categories = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(By.CLASS_NAME,'category'))

        categories = self.driver.find_elements(By.CLASS_NAME,'category')

        return choice([category for category in categories if category.text])

    def find_subcategory(self):
        subcategories = self.driver.find_elements(By.CLASS_NAME,'subcategory-name')
        if subcategories:
            return choice(subcategories)
        return None

    def find_product(self):
        return choice(self.driver.find_elements(By.CLASS_NAME,'product-miniature'))        

    def buy_product(self, quantity):
        click_counter = 0
        try:
            size = Select(self.driver.find_element(By.CLASS_NAME,'form-control'))
            choice(size.options).click()
            click_counter += 1
        except:
            pass

        colors = self.driver.find_elements(By.CLASS_NAME,'input-color')
        if len(colors) > 0:
            choice(colors).click()
            click_counter += 1

        amount = self.driver.find_element(By.ID,'quantity_wanted')

        amount.send_keys(Keys.CONTROL + "a")
        for i in str(quantity):
            amount.send_keys(i)
        amount.send_keys(Keys.ENTER)

        sleep(1)
        webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()

        for i in range(click_counter):
            sleep(0.1)
            self.driver.back()

    def buying_spree(self, quantity):
        for i in range(quantity):
            with Website(self.driver, self.find_category()):
                subcategory = self.find_subcategory()
                if subcategory:
                    with Website(self.driver, subcategory):
                        with Website(self.driver, self.find_product()):
                            self.buy_product(1)
                else:
                    with Website(self.driver, self.find_product()):
                        self.buy_product(1)

    def __del__(self):
        input('Press enter to exit')
        self.driver.quit()


if __name__ == "__main__":
    Customer().buying_spree(10)
    