import locators.locators


class SearchProductMainPage:
    def __init__(self, driver):
        self.driver = driver
        # Search product on main page elements
        self.search_product_on_main_page = locators.locators.MainPageLocators.search_product_input
        self.search_product_submit_button = locators.locators.MainPageLocators.search_product_button
        self.search_product_confirmation_msg = locators.locators.MainPageLocators.search_product_confirm_msg
        self.search_product_no_results_found_msg = locators.locators.MainPageLocators.search_product_no_results_found_msg

    def open_page(self):
        self.driver.get("http://automationpractice.com/index.php")

    def search_product(self, product):
        self.driver.find_element(*self.search_product_on_main_page).send_keys(product)

    def search_product_submit(self):
        self.driver.find_element(*self.search_product_submit_button).click()

    def search_product_confirm_msg(self):
        return self.driver.find_element(*self.search_product_confirmation_msg).text

    def search_product_no_results_were_found_msg(self):
        return self.driver.find_element(*self.search_product_no_results_found_msg).text
