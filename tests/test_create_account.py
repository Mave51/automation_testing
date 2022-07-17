import random
import time
import pytest
from pages.register_page import RegisterPage


@pytest.mark.usefixtures("test_setup")
class TestRegisterAccount:

    def test_create_account(self):
        email = str(random.randint(0, 10000)) + "testadresemail@gmail.com"
        register_page = RegisterPage(self.driver)
        register_page.open_page()
        register_page.register_account(email, "John", "Smith", "test098765432179", "6", "4", "1997", "John",
                                       "Smith", "Kwiatowa1", "Warsaw", "Alaska", "00000", "123456789", "Kwaiatowa1")
        time.sleep(2)
        assert 'Welcome to your account. Here you can manage all of your personal information and orders.' in register_page.get_welcome_to_account_msg()
