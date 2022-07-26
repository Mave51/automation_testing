import time

import pytest
from selenium.webdriver.support import wait

from pages.search_product_main_page import SearchProductMainPage


@pytest.mark.usefixtures("test_setup")
class TestSearchProduct:
    def test_order_product(self):
        search_product = SearchProductMainPage(self.driver)

        search_product.open_page()
        search_product.search_product("T shirt")
        search_product.search_product_submit()
        time.sleep(1)
        assert "1 result has been found." in search_product.search_product_confirm_msg()
