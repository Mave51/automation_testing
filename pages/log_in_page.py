from locators import locators


class LogInPage:
    def __init__(self, driver):
        self.driver = driver
        # Login page elements
        self.log_in_email = locators.LogInPageLocators.log_in_email_input
        self.log_in_password = locators.LogInPageLocators.log_in_password_input
        self.log_in_submit_button = locators.LogInPageLocators.log_in_submit_button
        self.user_logged_msg = locators.LogInPageLocators.user_logged_msg
        self.user_login_failed_msg = locators.LogInPageLocators.log_in_failed_msg

    def open_page(self):
        self.driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")

    def log_in(self, email, password):
        self.driver.find_element(*self.log_in_email).send_keys(email)
        self.driver.find_element(*self.log_in_password).send_keys(password)
        self.driver.find_element(*self.log_in_submit_button).click()

    def get_user_logged_msg(self):
        return self.driver.find_element(*self.user_logged_msg).text

    def get_user_log_in_failed_msg(self):
        return self.driver.find_element(*self.user_login_failed_msg).text
