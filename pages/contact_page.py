from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class ContactPage:
    def __init__(self, driver):
        self.driver = driver

        subject_heading_select = (By.ID, "id_contact")
        email_address_input = (By.ID, "email")
        order_reference_input = (By.ID, "id_order")
        leave_message_input = (By.ID, "message")
        submit_message_button = (By.ID, "submitMessage")
        message_successfully_sent_msg = (By.XPATH, "//p [text()='Your message has been successfully sent to our team']")

        # Contact page elements
        self.subject_heading = subject_heading_select
        self.email_address = email_address_input
        self.order_reference = order_reference_input
        self.leave_message = leave_message_input
        self.submit_message = submit_message_button
        self.message_sent_successfully = message_successfully_sent_msg

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
