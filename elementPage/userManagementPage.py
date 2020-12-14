from basePage.base_page import BasePage


class userManagementPage(BasePage):

    userMenu_loc = "xpath, //li[@class='el-menu-item is-active']"
    userName_loc = "css, [placeholder='用户名称']"
    phone_loc = "css, [placeholder='手机号']"
    stationName_loc = "css, [placeholder='岗位']"
    searchButton_loc = "xpath, //span[.='搜索']"
    resetButton_loc = "xpath, //span[.='重置']"
    addButton_loc = "xpath, //span[.='添加']"
    deleteButton_loc = "xpath, //span[.='删除']"
    selectAll_loc = "css, th.el-table_8_column_48 .el-checkbox__inner"
    select1_loc = "css, tbody > tr:nth-of-type(1) .el-checkbox__inner"
    select2_loc = "css, tbody > tr:nth-of-type(2) .el-checkbox__inner"
    update1_loc = "css, tbody > tr:nth-of-type(1) .edit-btn > span"
    update2_loc = "css, tbody > tr:nth-of-type(2) .edit-btn > span"
    delete1_loc = "css, tbody > tr:nth-of-type(1) .delete-btn > span"
    delete2_loc = "css, tbody > tr:nth-of-type(2) .delete-btn > span"
    tipsDeleteSuccess_loc = "css, .el-message"
    addUsername_loc = "css, form.el-form > .is-error > .el-form-item__content > .el-input > .el-input__inner"
    addUserPhone_loc = "css, input[maxlength='11']"
    addUserPassword_loc = "css, form.el-form > div:nth-of-type(3) .el-input__inner"
    addUserCheckPassword_loc = "css, form.el-form > div:nth-of-type(4) .el-input__inner"
    addUserStation_loc = "css, form.el-form > div:nth-of-type(5) [placeholder='请选择']"
    addUserStationSearch_loc = "xpath, //span[.='测试全权限']"
    addUserState_loc = "css, form.el-form > div:nth-of-type(6) [placeholder='请选择']"
    addUserStateSearch_loc = "xpath, //li[.='在职']"
    addUserBranch_loc = "css, form.el-form > .is-error [placeholder='请选择']"
    addUserBranchSearch_loc = "xpath, //span[.='事业部一']"
    addUserProject_loc = "css, form.el-form > .el-row [placeholder='请选择']"
    addUserProjectSearch_loc = "xpath, //span[.='测试项目1']"

    def switch_menu(self):
        self.find_element(self.userMenu_loc).click()

    def search_input_username(self, username):
        self.find_element(self.userName_loc).sendkeys(username)

    def search_input_phone(self, phone):
        self.find_element(self.phone_loc).sendkeys(phone)

    def search_input_station(self, stationName):
        self.find_element(self.stationName_loc).sendkeys(stationName)

    def check_select_all(self):
        self.find_element(self.selectAll_loc).click()

    def check_select_first(self):
        self.find_element(self.select1_loc).click()

    def check_select_second(self):
        self.find_element(self.select2_loc).click()

    def update_first(self):
        self.find_element(self.update1_loc).click()

    def update_second(self):
        self.find_element(self.update2_loc).click()

    def delete_first(self):
        self.find_element(self.delete1_loc).click()

    def delete_second(self):
        self.find_element(self.delete2_loc).click()

    def search_button(self):
        self.find_element(self.searchButton_loc).click()

    def reset_button(self):
        self.find_element(self.resetButton_loc).click()

    def add_button(self):
        self.find_element(self.addButton_loc).click()

    def delete_button(self):
        self.find_element(self.deleteButton_loc).click()

    def getTipsDeleteSuccess(self):
        return self.find_element(self.tipsDeleteSuccess_loc).text

    def inputAddUsername(self, username):
        self.find_element(self.addUsername_loc).sendkeys(username)

    def inputAddUserPhone(self, phone):
        self.find_element(self.addUserPhone_loc).sendkeys(phone)

    def inputAddUserPassword(self, password):
        self.find_element(self.addUserPassword_loc).sendkeys(password)

    def inputAddCheckPassword(self, password):
        self.find_element(self.addUserCheckPassword_loc).sendkeys(password)

    def inputAddUserStation(self):
        self.find_element(self.addUserStation_loc).click()

    def inputAddUserState(self):
        self.find_element(self.addUserState_loc).click()

    def inputUserBranch(self):
        self.find_element(self.addUserBranch_loc).click()
