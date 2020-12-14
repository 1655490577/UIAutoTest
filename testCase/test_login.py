from elementPage.loginPage import loginPage
import time
import pytest


class TestLogin:

    def test_login_success(self):
        test_obj = loginPage()
        test_obj.user_input('admin')
        test_obj.psw_input('admin')
        test_obj.login_button()
        time.sleep(0.5)
        url = test_obj.get_pageInfo('url')
        assert url == test_obj.base_url + '/gzy/organization'
        test_obj.close()

    @pytest.mark.parametrize(("name", "password"), [("", "admin"), ("admin", ""), ("", "")])
    def test_login_none_fail(self, name, password):
        test_obj = loginPage()
        test_obj.user_input(name)
        test_obj.psw_input(password)
        test_obj.login_button()
        time.sleep(0.5)
        assert test_obj.getTips_none() == '请输入账号或密码!'
        test_obj.close()

    def test_login_error_fail(self):
        test_obj = loginPage()
        test_obj.user_input('admin')
        test_obj.psw_input('213')
        test_obj.login_button()
        time.sleep(0.5)
        assert test_obj.getTips_error() == '手机号或密码不存在'
        test_obj.close()
