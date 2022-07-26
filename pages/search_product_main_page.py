from selenium.webdriver.common.by import By


class SearchProductMainPage:
    def __init__(self, driver):
        self.driver = driver

        search_product_input = (By.ID, "search_query_top")
        search_product_button = (By.NAME, "submit_search")
        search_product_confirm_msg = (By.XPATH, '//*[@id="center_column"]/h1/span[2]')
        search_product_no_results_found_msg = (By.XPATH, '//*[@id="center_column"]/p')

        # Search product on main page elements
        self.search_product_on_main_page = search_product_input
        self.search_product_submit_button = search_product_button
        self.search_product_confirmation_msg = search_product_confirm_msg
        self.search_product_no_results_found_msg = search_product_no_results_found_msg

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
