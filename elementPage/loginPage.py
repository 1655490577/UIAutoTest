from basePage.base_page import BasePage


class loginPage(BasePage):

    username_loc = "css, [placeholder='请输入手机号:']"
    pwd_loc = "css, [placeholder='请输入密码']"
    button_loc = "css, .el-button"
    tips_none_loc = "xpath, //p[@class='el-message__content']"
    tips_error_loc = "css, .el-message"

    def user_input(self, username):
        self.find_element(self.username_loc).send_keys(username)
        return username

    def psw_input(self, password):
        self.find_element(self.pwd_loc).send_keys(password)

    def login_button(self):
        self.find_element(self.button_loc).click()

    def getTips_none(self):
        return self.find_element(self.tips_none_loc).text

    def getTips_error(self):
        return self.find_element(self.tips_error_loc).text
