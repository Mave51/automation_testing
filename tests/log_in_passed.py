
import time
import pytest
from pages.log_in_page import LogInPage


@pytest.mark.usefixtures("setup")
class TestLoginPage:
    def test_log_in(self):
        log_in_page = LogInPage(self.driver)
        log_in_page.open_page()
        log_in_page.log_in("test1234554321@gmail.com", "test12345")
        time.sleep(1)
        assert 'Welcome to your account. Here you can manage all of your personal information and orders.' in log_in_page.get_user_logged_msg()

