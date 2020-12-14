from elementPage.loginPage import loginPage
import pytest


@pytest.fixture()
def login():
    test_first = loginPage()
    test_first.user_input('13100000001')
    test_first.psw_input('1')
    test_first.login_button()
