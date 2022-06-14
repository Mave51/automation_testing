from selenium.webdriver.support.select import Select

import locators.locators


class ContactPage:
    def __init__(self, driver):
        self.driver = driver
        # Contact page elements
        self.subject_heading = locators.locators.ContactPageLocators.subject_heading_select
        self.email_address = locators.locators.ContactPageLocators.email_address_input
        self.order_reference = locators.locators.ContactPageLocators.order_reference_input
        self.leave_message = locators.locators.ContactPageLocators.leave_message_input
        self.submit_message = locators.locators.ContactPageLocators.submit_message_button
        self.message_sent_successfully = locators.locators.ContactPageLocators.message_successfully_sent_msg

    def open_page(self):
        self.driver.get("http://automationpractice.com/index.php?controller=contact")

    def make_contact(self, subject, email, order_number, message):
        select_subject_heading = Select(self.driver.find_element(*self.subject_heading))
        select_subject_heading.select_by_visible_text(subject)
        self.driver.find_element(*self.email_address).send_keys(email)
        self.driver.find_element(*self.order_reference).send_keys(order_number)
        self.driver.find_element(*self.leave_message).send_keys(message)
        self.driver.find_element(*self.submit_message).click()

    def get_message_successfully_sent(self):
        return self.driver.find_element(*self.message_sent_successfully).text


