from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from random import choice, randint


class Website(object):
    def __init__(self, driver, element):
        self.driver = driver
        self.element = element
    
    def __enter__(self):
        self.element.click()

    def __exit__(self, *args):
        self.driver.back()


class Customer:
    WEBSITE = "https://localhost:4433"

    def __init__(self):
        options = Options()
        options.add_argument('ignore-certificate-errors')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.__get_website()

    def __del__(self):
        input('Press enter to exit')
        self.driver.quit()

    def __get_website(self):
        self.driver.get(self.WEBSITE)


    def find_category(self):
        try:
            WebDriverWait(self.driver, 1).until(lambda x: x.find_element(By.CLASS_NAME,'category'))
        except TimeoutException:
            self.__get_website()

        categories = self.driver.find_elements(By.CLASS_NAME,'category')

        return choice([category for category in categories if category.text])

    def find_subcategory(self):
        subcategories = self.driver.find_elements(By.CLASS_NAME,'subcategory-name')
        if subcategories:
            return choice(subcategories)
        return None

    def find_product(self):
        products = self.driver.find_elements(By.CLASS_NAME,'product-miniature')
        if products:
            return choice(products)
        return None       

    def buy_product(self, quantity):
        urls = set()
        urls.add(self.driver.current_url)

        size_form = self.driver.find_element(By.CLASS_NAME,'form-control')

        if size_form.tag_name == 'select':
            size = Select(size_form)
            choice(size.options).click()
            urls.add(self.driver.current_url)

        colors = self.driver.find_elements(By.CLASS_NAME,'input-color')

        if colors:
            choice(colors).click()
            urls.add(self.driver.current_url)

        amount = self.driver.find_element(By.ID,'quantity_wanted')

        amount.send_keys(Keys.CONTROL + "a")
        for i in str(quantity):
            amount.send_keys(i)
        amount.send_keys(Keys.ENTER)

        sleep(1)
        webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        urls.add(self.driver.current_url)

        for _ in range(len(urls)-1):
            sleep(0.1)
            self.driver.back()

    def buying_spree(self, quantity, products_range=(1,1)):
        for i in range(quantity):
            with Website(self.driver, self.find_category()):
                subcategory = self.find_subcategory()
                if subcategory:
                    with Website(self.driver, subcategory):
                        with Website(self.driver, self.find_product()):
                            self.buy_product(randint(*products_range))
                else:
                    with Website(self.driver, self.find_product()):
                        self.buy_product(randint(*products_range))

    def shopping_cart(self):
        self.driver.find_element(By.CLASS_NAME,'cart-preview').click()
        delete = self.driver.find_elements(By.CLASS_NAME,'remove-from-cart')
        if delete:
            choice(delete).click()

    def checkout(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME,'btn-primary')))
        self.driver.find_element(By.CLASS_NAME,'btn-primary').click()

        self.driver.find_element(By.ID,'field-address1').send_keys('ul. Testowa 4/420')
        self.driver.find_element(By.ID,'field-postcode').send_keys('80-420')
        self.driver.find_element(By.ID,'field-city').send_keys('Testowo')

        self.driver.find_element(By.NAME,'confirm-addresses').click()

        self.driver.find_element(By.CSS_SELECTOR, "label[for='delivery_option_2']").click()

        self.driver.find_element(By.NAME,'confirmDeliveryOption').click()

        self.driver.find_element(By.ID,'payment-option-1').click()
        self.driver.find_element(By.ID,'conditions_to_approve[terms-and-conditions]').click()

        self.driver.find_element(By.ID,'payment-confirmation').find_element(By.TAG_NAME,'button').click()

    def __fill_account_form(self):
        self.driver.find_element(By.CLASS_NAME,'radio-inline').click()
        self.driver.find_element(By.ID,'field-firstname').send_keys('Jan')
        self.driver.find_element(By.ID,'field-lastname').send_keys('Kowalski')
        self.driver.find_element(By.ID,'field-email').send_keys('jan.kowal@gmail.com')
        self.driver.find_element(By.ID,'field-password').send_keys('2uPer4as1o')
        self.driver.find_element(By.ID,'field-birthday').send_keys('2000-01-01')

    def create_account(self):
        self.driver.find_element(By.CLASS_NAME,'user-info').click()
        self.driver.find_element(By.CLASS_NAME,'no-account').click()

        self.__fill_account_form()

        self.driver.find_element(By.NAME,'customer_privacy').click()

        self.driver.find_element(By.CLASS_NAME,'btn-primary').click()

    def check_order_status(self):
        self.__get_website()
        self.driver.find_element(By.CLASS_NAME,'user-info').find_element(By.CLASS_NAME,'account').click()
        self.driver.find_element(By.ID,'history-link').click()

        self.driver.find_element(By.CLASS_NAME,'view-order-details-link').click()

if __name__ == "__main__":
    customer = Customer()
    customer.create_account()
    customer.buying_spree(5,(1,4))
    customer.shopping_cart()
    customer.checkout()
    customer.check_order_status()
    