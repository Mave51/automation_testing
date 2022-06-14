from selenium.webdriver.support.select import Select

from locators import locators


class RegisterPage:

    def __init__(self, driver):
        self.driver = driver
        # Register Page Elements
        self.reg_email_input = locators.RegisterPageLocators.reg_email_input
        self.reg_submit_button = locators.RegisterPageLocators.reg_submit_button
        self.reg_title_gender = locators.RegisterPageLocators.reg_title_gender
        self.reg_first_name_input = locators.RegisterPageLocators.reg_first_name_input
        self.reg_last_name_input = locators.RegisterPageLocators.reg_last_name_input
        self.reg_password_input = locators.RegisterPageLocators.reg_password_input
        self.reg_day_of_birth_select = locators.RegisterPageLocators.reg_day_of_birth_select
        self.reg_month_of_birth_select = locators.RegisterPageLocators.reg_month_of_birth_select
        self.reg_year_of_birth_select = locators.RegisterPageLocators.reg_year_of_birth_select
        self.reg_address_first_name_input = locators.RegisterPageLocators.reg_address_first_name_input
        self.reg_address_last_name_input = locators.RegisterPageLocators.reg_address_last_name_input
        self.reg_address_address_input = locators.RegisterPageLocators.reg_address_address_input
        self.reg_address_city_input = locators.RegisterPageLocators.reg_address_city_input
        self.reg_address_state_select = locators.RegisterPageLocators.reg_address_state_select
        self.reg_address_post_code_input = locators.RegisterPageLocators.reg_address_post_code_input
        self.reg_address_phone_number_input = locators.RegisterPageLocators.reg_address_phone_number_input
        self.reg_address_alias_for_reference_input = locators.RegisterPageLocators.reg_address_alias_for_reference_input
        self.reg_register_account_button = locators.RegisterPageLocators.reg_register_account_button
        self.welcome_to_account_msg = locators.RegisterPageLocators.welcome_to_account_msg

    def open_page(self):
        self.driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")

    def register_account(self, email, first_name, last_name, password, day_of_birth, month_of_birth, year_of_birth,
                         address_first_name, address_last_name, address_address, address_city, address_state,
                         address_post_code, address_phone_number, address_alias):
        self.driver.find_element(*self.reg_email_input).send_keys(email)
        self.driver.find_element(*self.reg_submit_button).click()
        self.driver.find_element(*self.reg_title_gender).click()
        self.driver.find_element(*self.reg_first_name_input).send_keys(first_name)
        self.driver.find_element(*self.reg_last_name_input).send_keys(last_name)
        self.driver.find_element(*self.reg_password_input).send_keys(password)
        select_day_of_birth = Select(self.driver.find_element(*self.reg_day_of_birth_select))
        select_day_of_birth.select_by_value(day_of_birth)
        select_month_of_birth = Select(self.driver.find_element(*self.reg_month_of_birth_select))
        select_month_of_birth.select_by_index(month_of_birth)
        select_year_of_birth = Select(self.driver.find_element(*self.reg_year_of_birth_select))
        select_year_of_birth.select_by_value(year_of_birth)
        self.driver.find_element(*self.reg_address_first_name_input).send_keys(address_first_name)
        self.driver.find_element(*self.reg_address_last_name_input).send_keys(address_last_name)
        self.driver.find_element(*self.reg_address_address_input).send_keys(address_address)
        self.driver.find_element(*self.reg_address_city_input).send_keys(address_city)
        select_state = Select(self.driver.find_element(*self.reg_address_state_select))
        select_state.select_by_visible_text(address_state)
        self.driver.find_element(*self.reg_address_post_code_input).send_keys(address_post_code)
        self.driver.find_element(*self.reg_address_phone_number_input).send_keys(address_phone_number)
        self.driver.find_element(*self.reg_address_alias_for_reference_input).send_keys(address_alias)
        self.driver.find_element(*self.reg_register_account_button).click()

    def get_welcome_to_account_msg(self):
        return self.driver.find_element(*self.welcome_to_account_msg).text
