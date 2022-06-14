import pytest

from pages.contact_page import ContactPage


@pytest.mark.usefixtures("setup")
class TestMakeContact:
    def test_make_contact(self):
        contact_page = ContactPage(self.driver)
        contact_page.open_page()
        contact_page.make_contact("Customer service", "test123@gmail.com", "1234567890", "This is test message for make contact with customer service")
        assert "Your message has been successfully sent to our team." in contact_page.get_message_successfully_sent()
