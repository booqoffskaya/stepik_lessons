from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
import time

link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'


def get_random_email_password():
    email = str(time.time()) + "@fakemail.org"
    password = str(time.time())
    return email, password


@pytest.fixture(scope="function")
def new_user(browser):
    page = LoginPage(browser, link)
    page.open()
    email, password = get_random_email_password()
    page.register_new_user(email, password)
    page.logout()
    return email, password


@pytest.mark.personal_tests
class TestRegisterFromLoginPage:
    def test_guest_can_register(self, browser):
        page = LoginPage(browser, link)
        page.open()
        email, password = get_random_email_password()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_register_twice(self, browser, new_user):
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(*new_user)
        page.should_be_login_page()
        page.should_be_register_form_danger_alert()


@pytest.mark.personal_tests
class TestLoginFromLoginPage:
    def test_user_can_login(self, browser, new_user):
        page = LoginPage(browser, link)
        page.open()
        page.login(*new_user)
        page.should_be_authorized_user()

    def test_guest_cant_login_with_non_existent_email(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.login(*get_random_email_password())
        page.should_be_login_page()
        page.should_be_login_form_danger_alert()

    def test_guest_cant_login_with_wrong_password(self, browser, new_user):
        page = LoginPage(browser, link)
        page.open()
        email, password = new_user
        page.login(email, 'wrong_password')
        page.should_be_login_page()
        page.should_be_login_form_danger_alert()


@pytest.mark.personal_tests
class TestLoginPage:
    def test_guest_cant_see_product_in_basket_opened_from_login_page(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_basket_page()
        basket_page.should_be_empty_basket_text()
        basket_page.should_not_be_basket_items()
