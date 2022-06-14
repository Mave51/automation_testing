import time

import pytest

from pages.log_in_page import LogInPage


@pytest.mark.usefixtures("setup")
class TestLoginPage:
    def test_log_in(self):
        log_in_page = LogInPage(self.driver)
        log_in_page.open_page()
        log_in_page.log_in("test123455432179@gmail.com", "test123455")
        time.sleep(1)
        assert 'Authentication failed.' in log_in_page.get_user_log_in_failed_msg()
