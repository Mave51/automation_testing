import locators.locators


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        # Main page elements
        self.newsletter_subscribe = locators.locators.NewsletterLocators.email_address
        self.submit_subscribe_btn = locators.locators.NewsletterLocators.submit_newsletter_button
        self.newsletter_subscribed_successfully_msg = locators.locators.NewsletterLocators.newsletter_subscribed_successfully
        self.newsletter_not_subscribed_error_msg = locators.locators.NewsletterLocators.newsletter_not_subscribed_error

    def open_page(self):
        self.driver.get("http://automationpractice.com/index.php")

    def subscribe_to_the_newsletter(self, email):
        self.driver.find_element(*self.newsletter_subscribe).send_keys(email)

    def submit_subscribe(self):
        self.driver.find_element(*self.submit_subscribe_btn).click()

    def get_newsletter_subscribed_successfully_msg(self):
        return self.driver.find_element(*self.newsletter_subscribed_successfully_msg).text

    def get_newsletter_not_subscribed_error_msg(self):
        return self.driver.find_element(*self.newsletter_not_subscribed_error_msg).text
