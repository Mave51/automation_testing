from selenium.webdriver import ActionChains

from locators import locators


class ShoppingMainPage:
    def __init__(self, driver):
        self.driver = driver
        # Shopping Main Page Elements
        self.add_to_cart = locators.MainPageLocators.add_to_cart_button
        self.description_of_product = locators.MainPageLocators.description_of_product_span
        self.proceed_to_checkout = locators.MainPageLocators.proceed_to_checkout_button
        self.proceed_to_checkout_in_cart = locators.MainPageLocators.proceed_to_checkout_in_cart_button
        self.proceed_to_checkout_when_user_logged = locators.MainPageLocators.proceed_to_checkout_when_user_logged_button
        self.terms_of_service_agreement = locators.MainPageLocators.terms_of_service_agreement_checkbox
        self.proceed_to_checkout_after_choosing_delivery = locators.MainPageLocators.proceed_to_checkout_after_choosing_delivery_span
        self.choose_payment = locators.MainPageLocators.choose_payment_span
        self.confirm_order = locators.MainPageLocators.confirm_order_span
        self.order_is_complete_msg = locators.MainPageLocators.order_is_complete_msg

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
