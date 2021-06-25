from selenium.webdriver.common.by import By


class LoginPageLocators:
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form button[type='submit']")
    PRODUCT_NAME = (By.CSS_SELECTOR, "article.product_page h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "article.product_page p.price_color")
    ALERT_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages :nth-child(1) strong")
    ALERT_BASKET_TOTAL = (By.CSS_SELECTOR, "#messages :nth-child(3) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages :nth-child(1) .alertinner")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini  a.btn")


class BasketPageLocators():
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, ".page_inner p")
    BASKET_ITEMS = (By.CSS_SELECTOR, "div.basket-items")
