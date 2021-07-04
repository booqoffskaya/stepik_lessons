from selenium.webdriver.common.by import By
from .base_page import BasePage

from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def check_name_of_added_product(self, name):
        assert name == self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_NAME).text, \
            "The name of the added product does not match the expected name"

    def check_basket_total_price(self, price):
        assert price == self.browser.find_element(*ProductPageLocators.ALERT_BASKET_TOTAL).text, \
            "The basket total price does not match the expected total price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"

    def should_not_be_success_message_after_timeout(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
