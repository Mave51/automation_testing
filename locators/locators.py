from selenium.webdriver.common.by import By


class RegisterPageLocators:
    reg_email_input = (By.ID, "email_create")
    reg_submit_button = (By.ID, "SubmitCreate")
    reg_title_gender = (By.ID, "id_gender1")
    reg_first_name_input = (By.ID, "customer_firstname")
    reg_last_name_input = (By.ID, "customer_lastname")
    reg_password_input = (By.ID, "passwd")
    reg_day_of_birth_select = (By.ID, "days")
    reg_month_of_birth_select = (By.ID, "months")
    reg_year_of_birth_select = (By.ID, "years")
    reg_address_first_name_input = (By.ID, "firstname")
    reg_address_last_name_input = (By.ID, "lastname")
    reg_address_address_input = (By.ID, "address1")
    reg_address_city_input = (By.ID, "city")
    reg_address_state_select = (By.ID, "id_state")
    reg_address_post_code_input = (By.ID, "postcode")
    reg_address_phone_number_input = (By.ID, "phone_mobile")
    reg_address_alias_for_reference_input = (By.ID, "alias")
    reg_register_account_button = (By.ID, "submitAccount")
    welcome_to_account_msg = (By.XPATH, "//p [@class='info-account']")


class LogInPageLocators:
    log_in_email_input = (By.ID, "email")
    log_in_password_input = (By.ID, "passwd")
    log_in_submit_button = (By.ID, "SubmitLogin")
    user_logged_msg = (By.XPATH, "//p [@class='info-account']")
    log_in_failed_msg = (By.XPATH, "//li [text()='Authentication failed.']")


class MainPageLocators:
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
    search_product_input = (By.ID, "search_query_top")
    search_product_button = (By.NAME, "submit_search")
    search_product_confirm_msg = (By.XPATH, '//*[@id="center_column"]/h1/span[2]')
    search_product_no_results_found_msg = (By.XPATH, '//*[@id="center_column"]/p')


class ContactPageLocators:
    subject_heading_select = (By.ID, "id_contact")
    email_address_input = (By.ID, "email")
    order_reference_input = (By.ID, "id_order")
    leave_message_input = (By.ID, "message")
    submit_message_button = (By.ID, "submitMessage")
    message_successfully_sent_msg = (By.XPATH, "//p [text()='Your message has been successfully sent to our team']")


class NewsletterLocators:
    email_address = (By.ID, "newsletter-input")
    submit_newsletter_button = (By.NAME, "submitNewsletter")
    newsletter_subscribed_successfully = (By.XPATH, "/html/body/div/div[2]/div/p")
    newsletter_not_subscribed_error = (By.XPATH, "/html/body/div/div[2]/div/p")
