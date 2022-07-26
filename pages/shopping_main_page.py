from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class ShoppingMainPage:
    def __init__(self, driver):
        self.driver = driver

        add_to_cart_button = (By.XPATH, "//*[@id='homefeatured']/li[1]/div/div[2]/div[2]/a[1]/span")
        description_of_product_span = (By.XPATH, '//*[@id="homefeatured"]/li[1]/div/div[2]/h5/a')
        proceed_to_checkout_button = (By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a/span')
        proceed_to_checkout_in_cart_button = (
            By.XPATH, "//a [@class='button btn btn-default standard-checkout button-medium']")
        proceed_to_checkout_when_user_logged_button = (By.XPATH, '//*[@id="center_column"]/form/p/button/span')
        terms_of_service_agreement_checkbox = (By.ID, 'cgv')
        proceed_to_checkout_after_choosing_delivery_span = (By.XPATH, '//*[@id="form"]/p/button/span')
        choose_payment_span = (By.XPATH, '//*[@id="HOOK_PAYMENT"]/div[1]/div/p/a')
        confirm_order_span = (By.XPATH, "// button[@class='button btn btn-default button-medium']")
        order_is_complete_msg = (By.XPATH, '//*[@id="center_column"]/div/p/strong')

        # Shopping Main Page Elements
        self.add_to_cart = add_to_cart_button
        self.description_of_product = description_of_product_span
        self.proceed_to_checkout = proceed_to_checkout_button
        self.proceed_to_checkout_in_cart = proceed_to_checkout_in_cart_button
        self.proceed_to_checkout_when_user_logged = proceed_to_checkout_when_user_logged_button
        self.terms_of_service_agreement = terms_of_service_agreement_checkbox
        self.proceed_to_checkout_after_choosing_delivery = proceed_to_checkout_after_choosing_delivery_span
        self.choose_payment = choose_payment_span
        self.confirm_order = confirm_order_span
        self.order_is_complete_msg = order_is_complete_msg

    def open_page(self):
        self.driver.get("http://automationpractice.com/index.php")

    def move_to_element(self):
        action = ActionChains(self.driver)
        element = self.driver.find_element(*self.description_of_product)
        action.move_to_element(element).perform()

    def add_product_to_cart(self):
        self.driver.find_element(*self.add_to_cart).click()

    def go_to_checkout(self):
        self.driver.find_element(*self.proceed_to_checkout).click()

    def go_to_checkout_after_summary(self):
        self.driver.find_element(*self.proceed_to_checkout_in_cart).click()

    def proceed_checkout_after_sign_in(self):
        self.driver.find_element(*self.proceed_to_checkout_when_user_logged).click()

    def mark_terms_of_service_agreement(self):
        self.driver.find_element(*self.terms_of_service_agreement).click()

    def go_to_payment(self):
        self.driver.find_element(*self.proceed_to_checkout_after_choosing_delivery).click()

    def choose_way_of_payment(self):
        self.driver.find_element(*self.choose_payment).click()

    def confirm_your_order(self):
        self.driver.find_element(*self.confirm_order).click()

    def get_order_confirmation(self):
        return self.driver.find_element(*self.order_is_complete_msg).text
