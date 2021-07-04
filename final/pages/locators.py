from selenium.webdriver.common.by import By


class LoginPageLocators:
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "[name='registration-email']")
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "[name='registration-password1']")
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "[name='registration-password2']")
    REGISTRATION_SUBMIT = (By.CSS_SELECTOR, "[name='registration_submit']")

    LOGIN_EMAIL = (By.CSS_SELECTOR, "[name='login-username']")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "[name='login-password']")
    LOGIN_SUBMIT = (By.CSS_SELECTOR, "[name='login_submit']")

    REGISTER_FORM_ALERT_DANGER = (By.CSS_SELECTOR, '.register_form div.alert.alert-danger')
    LOGIN_FORM_ALERT_DANGER = (By.CSS_SELECTOR, '.login_form div.alert.alert-danger')


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
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGOUT_LINK = (By.ID, "logout_link")


class BasketPageLocators():
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, ".page_inner p")
    BASKET_ITEMS = (By.CSS_SELECTOR, "div.basket-items")
