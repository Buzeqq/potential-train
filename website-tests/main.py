from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from random import choice, randint
from faker import Faker


class Website(object):
    def __init__(self, driver, element):
        self.driver = driver
        self.element = element
    
    def __enter__(self):
        self.return_web = self.driver.current_url
        self.element.click()

    def __exit__(self, *args):
        self.driver.get(self.return_web)


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


    def __find_category(self):
        try:
            WebDriverWait(self.driver, 1).until(lambda x: x.find_element(By.CLASS_NAME,'category'))
        except TimeoutException:
            self.__get_website()

        categories = [category for category in self.driver.find_elements(By.CLASS_NAME,'category') if category.text]

        for i in range(len(categories)):
            try:
                WebDriverWait(self.driver, 1).until(lambda x: x.find_element(By.CLASS_NAME,'category'))
            except TimeoutException:
                self.__get_website()

            categories = [category for category in self.driver.find_elements(By.CLASS_NAME,'category') if category.text]

            yield categories[i]

    def __find_subcategory(self, limit=3):
        subcategories = self.driver.find_elements(By.CLASS_NAME,'subcategory-name')

        for i in range(min(len(subcategories),limit)):
            subcategories = self.driver.find_elements(By.CLASS_NAME,'subcategory-name')
            yield subcategories[i]

    def __find_product(self, limit=5):
        products = self.driver.find_elements(By.CLASS_NAME,'product-miniature')

        for i in range(min(len(products),limit)):
            products = self.driver.find_elements(By.CLASS_NAME,'product-miniature')

            yield products[i]  

    def __buy_product(self, quantity):
        size_form = self.driver.find_element(By.CLASS_NAME,'form-control')

        if size_form.tag_name == 'select':
            size = Select(size_form)
            choice(size.options).click()

        colors = self.driver.find_elements(By.CLASS_NAME,'input-color')

        if colors:
            choice(colors).click()

        amount = self.driver.find_element(By.ID,'quantity_wanted')

        amount.send_keys(Keys.CONTROL + "a")
        for i in str(quantity):
            amount.send_keys(i)

        sleep(1)
        amount.send_keys(Keys.ENTER)

        sleep(1)
        webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()

    def buying_spree(self, quantity, products_range=(1,1)):
        for category in self.__find_category():
            with Website(self.driver, category):
                for subcategory in self.__find_subcategory(limit=3):
                    with Website(self.driver, subcategory):
                        for product in self.__find_product(limit=quantity):
                            sleep(0.5)
                            with Website(self.driver, product):
                                self.__buy_product(randint(*products_range))

    def shopping_cart(self):
        self.driver.find_element(By.CLASS_NAME,'cart-preview').click()
        delete = self.driver.find_elements(By.CLASS_NAME,'remove-from-cart')
        if delete:
            choice(delete).click()

    def checkout(self):
        button = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME,'btn-primary')))
        button.click()

        self.driver.find_element(By.ID,'field-address1').send_keys('ul. Testowa 4/420')
        self.driver.find_element(By.ID,'field-postcode').send_keys('80-420')
        self.driver.find_element(By.ID,'field-city').send_keys('Testowo')

        self.driver.find_element(By.NAME,'confirm-addresses').click()

        self.driver.find_element(By.CSS_SELECTOR, "label[for='delivery_option_6']").click()

        self.driver.find_element(By.NAME,'confirmDeliveryOption').click()

        self.driver.find_element(By.ID,'payment-option-2').click()
        self.driver.find_element(By.ID,'conditions_to_approve[terms-and-conditions]').click()

        self.driver.find_element(By.ID,'payment-confirmation').find_element(By.TAG_NAME,'button').click()

    def __fill_account_form(self):
        fake = Faker()
        self.driver.find_element(By.CLASS_NAME,'radio-inline').click()
        self.driver.find_element(By.ID,'field-firstname').send_keys(fake.first_name())
        self.driver.find_element(By.ID,'field-lastname').send_keys(fake.last_name())
        self.driver.find_element(By.ID,'field-email').send_keys(fake.email())
        self.driver.find_element(By.ID,'field-password').send_keys('2uPer4as1o')
        self.driver.find_element(By.ID,'field-birthday').send_keys('2000-01-01')

    def create_account(self):
        self.driver.find_element(By.CLASS_NAME,'user-info').click()
        self.driver.find_element(By.CLASS_NAME,'no-account').click()

        self.__fill_account_form()

        self.driver.find_element(By.NAME,'customer_privacy').click()

        self.driver.find_element(By.CLASS_NAME,'btn-primary').click()

        try:
            self.driver.find_element(By.CLASS_NAME,'alert-danger')
            raise Exception('Account already exists')
        except NoSuchElementException:
            pass

    def check_order_status(self):
        self.__get_website()
        self.driver.find_element(By.CLASS_NAME,'user-info').find_element(By.CLASS_NAME,'account').click()
        self.driver.find_element(By.ID,'history-link').click()

        self.driver.find_element(By.CLASS_NAME,'view-order-details-link').click()


def task(job, description, success, args=()):
    if success:
        try:
            job(*args)
        except Exception as e:
            print(e.__class__)
            print(e)
            success = False

    print(description, ': ✅' if success else ': ❌')
    return success


if __name__ == "__main__":
    customer = Customer()
    tests = True
    for job in [customer.create_account ,customer.buying_spree, customer.shopping_cart, customer.checkout, customer.check_order_status]:
        tests =task(job, job.__name__, success=tests, args=(3,(1,4)) if job.__name__ == 'buying_spree' else ())
    