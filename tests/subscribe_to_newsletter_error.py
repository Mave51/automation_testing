
import time

import pytest

from pages.main_page import MainPage


@pytest.mark.usefixtures("setup")
class TestSubscribeToNewsletter:
    def test_subscribe_to_the_newsletter(self):

        subscribe_to_newsletter = MainPage(self.driver)
        subscribe_to_newsletter.open_page()
        subscribe_to_newsletter.subscribe_to_the_newsletter("test123@wp.pl")
        subscribe_to_newsletter.submit_subscribe()
        time.sleep(1)
        assert "Newsletter : This email address is already registered." in subscribe_to_newsletter.get_newsletter_not_subscribed_error_msg()