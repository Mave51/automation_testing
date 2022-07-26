import time

import pytest

from pages.search_product_main_page import SearchProductMainPage


@pytest.mark.usefixtures("test_setup")
class TestSearchProduct:
    def test_order_product(self):
        search_product = SearchProductMainPage(self.driver)

        search_product.open_page()
        search_product.search_product("Pants")
        search_product.search_product_submit()
        time.sleep(1)
        assert "No results were found for your search" in search_product.search_product_no_results_were_found_msg()
