from selenium.webdriver.common.by import By


class LoginPageLocators:
    register_form = '#register_form'
    login_form = '#login_form'


class ProductPageLocators:
    add_to_basket_button = "#add_to_basket_form button[type='submit']"
    product_name = "article.product_page h1"
    product_price = "article.product_page p.price_color"
    alert_product_name = "#messages :nth-child(1) strong"
    alert_basket_total = "#messages :nth-child(3) strong"
    success_message = "#messages :nth-child(1) .alertinner"


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

