import random
import time

import pytest

from pages.main_page import MainPage


@pytest.mark.usefixtures("setup")
class TestSubscribeToNewsletter:
    def test_subscribe_to_the_newsletter(self):
        email = str(random.randint(0, 10000)) + "testadresemail@gmail.com"

        subscribe_to_newsletter = MainPage(self.driver)
        subscribe_to_newsletter.open_page()
        time.sleep(1)
        subscribe_to_newsletter.subscribe_to_the_newsletter(email)
        time.sleep(1)
        subscribe_to_newsletter.submit_subscribe()
        time.sleep(1)
        assert "Newsletter : You have successfully subscribed to this newsletter." in subscribe_to_newsletter.get_newsletter_subscribed_successfully_msg()
