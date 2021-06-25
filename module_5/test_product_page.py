import pytest
import time
from .pages.product_page import ProductPage

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo='


class TestProductPage:
    @pytest.mark.parametrize('promo_offer',
                             ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6",
                              pytest.param("offer7", marks=pytest.mark.xfail),
                              "offer8", "offer9"])
    def test_guest_can_add_product_to_basket(self, browser, promo_offer):
        print(promo_offer)
        promo_link = link + promo_offer
        page = ProductPage(browser, promo_link)
        page.open()
        product_name = page.get_product_name()
        product_price = page.get_product_price()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.check_name_of_added_product(product_name)
        page.check_basket_total_price(product_price)

