import time

import pytest
from pages.log_in_page import LogInPage
from pages.shopping_main_page import ShoppingMainPage


@pytest.mark.usefixtures("setup")
class TestOrderProductPage:
    def test_order_product(self):
        order_the_product = ShoppingMainPage(self.driver)
        log_in_page = LogInPage(self.driver)

        order_the_product.open_page()
        order_the_product.move_to_element()
        order_the_product.add_product_to_cart()
        order_the_product.go_to_checkout()
        time.sleep(1)
        order_the_product.go_to_checkout_after_summary()
        time.sleep(1)
        log_in_page.log_in("test1234554321@gmail.com", "test12345")
        order_the_product.proceed_checkout_after_sign_in()
        order_the_product.mark_terms_of_service_agreement()
        order_the_product.go_to_payment()
        order_the_product.choose_way_of_payment()
        time.sleep(1)
        order_the_product.confirm_your_order()
        assert "Your order on My Store is complete." in order_the_product.get_order_confirmation()
