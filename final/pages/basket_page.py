from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()

    def should_be_basket_url(self):
        assert 'basket' in self.browser.current_url

    def should_be_empty_basket_text(self):
        assert "Your basket is empty." in self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT).text, \
            "Empty basket text is not presented, but should be "

    def should_not_be_basket_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket items are presented, but should not be"