import pytest
from pages.main_page import MainPage


link = "http://selenium1py.pythonanywhere.com/"


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
    #page.go_to_login_page()
