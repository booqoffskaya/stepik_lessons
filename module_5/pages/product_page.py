from selenium.webdriver.common.by import By
from .base_page import BasePage

from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(By.CSS_SELECTOR, ProductPageLocators.add_to_basket_button)
        add_to_basket_button.click()

    def get_product_name(self):
        return self.browser.find_element(By.CSS_SELECTOR, ProductPageLocators.product_name).text

    def get_product_price(self):
        return self.browser.find_element(By.CSS_SELECTOR, ProductPageLocators.product_price).text

    def get_basket_total(self):
        return self.browser.find_element(By.CSS_SELECTOR, ProductPageLocators.basket_total).text

    def check_name_of_added_product(self, name):
        assert name == self.browser.find_element(By.CSS_SELECTOR, ProductPageLocators.alert_product_name).text

    def check_basket_total_price(self, price):
        assert price == self.browser.find_element(By.CSS_SELECTOR, ProductPageLocators.alert_basket_total).text
