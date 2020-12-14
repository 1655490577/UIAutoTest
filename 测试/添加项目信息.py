from selenium import webdriver
from faker import Faker
import time


fake = Faker('zh_CN')
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://manage.supervisor.dev.hfhksoft.com/')
driver.implicitly_wait(3)
driver.find_element_by_css_selector("[placeholder='请输入手机号:']").clear()
driver.find_element_by_css_selector("[placeholder='请输入手机号:']").send_keys('13168775547')
driver.implicitly_wait(3)
driver.find_element_by_css_selector("[placeholder='请输入密码']").clear()
driver.find_element_by_css_selector("[placeholder='请输入密码']").send_keys('1')
driver.implicitly_wait(3)
driver.find_element_by_xpath("//span[.='登录']").click()
driver.implicitly_wait(3)
driver.find_element_by_xpath("//span[.='项目信息管理']").click()
driver.implicitly_wait(3)
driver.find_element_by_css_selector("ul[data-old-padding-top] > div:nth-of-type(1) .el-menu-item").click()
driver.implicitly_wait(3)
# driver.find_element_by_xpath("//span[.='添加项目']").click()
# driver.implicitly_wait(3)

for p in range(2):
    projectInfo = {
        'projectName': f'测试项目{p+1}',
        'projectAddress': fake.address(),
        'build': str(fake.pyfloat(left_digits=None, right_digits=2, positive=False, min_value=0, max_value=None)),
        'days': fake.pyint(min_value=0, max_value=9999, step=1),
        'projectCompany': fake.company(),
        'projectPeople': fake.name(),
        'projectPhone': fake.phone_number(),
    }
    driver.find_element_by_xpath("//span[.='添加项目']").click()
    driver.implicitly_wait(3)
    driver.find_element_by_css_selector("[placeholder='请输入项目名称:']").send_keys(projectInfo['projectName'])
    driver.implicitly_wait(3)
    driver.find_element_by_css_selector("[placeholder='请输入项目地址:']").send_keys(projectInfo['projectAddress'])
    driver.implicitly_wait(3)
    driver.find_element_by_css_selector("form.el-form > div:nth-of-type(4) .el-select__caret").click()
    driver.find_element_by_xpath("//li[.='住宅']").click()
    driver.implicitly_wait(3)
    driver.find_element_by_css_selector("form.el-form > div:nth-of-type(5) .el-select__caret").click()
    driver.find_element_by_xpath("//li[.='住宅用途']").click()
    driver.find_element_by_css_selector("[placeholder='请选择所属事业部:']").click()
    time.sleep(0.5)
    aList = driver.find_elements_by_css_selector("div[x-placement='bottom-start'] .el-select-dropdown__wrap .el-select-dropdown__item")
    driver.implicitly_wait(3)
    aList[2].click()
    driver.find_element_by_css_selector("[placeholder='请输入建筑面积:']").send_keys(projectInfo['build'])
    driver.find_element_by_css_selector("[placeholder='选择日期'][name]").click()
    time.sleep(0.5)
    driver.find_element_by_xpath("//span[contains(.,'此刻')]").click()
    # driver.find_element_by_css_selector("table.el-date-table .today span").click()
    # driver.find_element_by_css_selector("button.is-plain > span").click()
    driver.find_element_by_css_selector("[placeholder='请输入总工期:']").send_keys(projectInfo['days'])
    driver.find_element_by_css_selector("[placeholder='请输入建设单位:']").send_keys(projectInfo['projectCompany'])
    driver.find_element_by_css_selector("[placeholder='请输入联系人:']").send_keys(projectInfo['projectPeople'])
    driver.find_element_by_css_selector("[placeholder='请输入联系电话:']").send_keys(projectInfo['projectPhone'])
    driver.find_element_by_xpath("//span[.='保存进行下一步']").click()
    # 添加标段
    for i in range(3):
        bidInfo = {
            'bidName': f'标段{i+1}',
            'bidArea': str(fake.pyfloat(left_digits=None, right_digits=2, positive=False, min_value=0, max_value=None)),
            'bidPeople': fake.name(),
            'bidPhone': fake.phone_number(),
            'bidUnit1': fake.company(),
            'bidUnit2': fake.company(),
            'bidUnit3': fake.company(),
            'bidUnit4': fake.company(),
            'bidUnit5': fake.company()
        }
        driver.find_element_by_xpath("//span[.='添加标段']").click()
        driver.find_element_by_css_selector("[placeholder='标段名称']").send_keys(bidInfo['bidName'])
        driver.find_element_by_css_selector("[placeholder='建筑面积']").send_keys(bidInfo['bidArea'])
        driver.find_element_by_css_selector("div.el-dialog__body .is-required [placeholder='联系人']").send_keys(bidInfo['bidPeople'])
        driver.find_element_by_css_selector("div.el-dialog__body .is-required [placeholder='联系电话']").send_keys(bidInfo['bidPhone'])
        driver.find_element_by_xpath("//span[.='添加单位']").click()
        driver.find_element_by_css_selector("div.el-dialog__body form:nth-of-type(1) [placeholder='单位名称']").send_keys(bidInfo['bidUnit1'])
        driver.find_element_by_css_selector("div.el-dialog__body form:nth-of-type(2) [placeholder='单位名称']").send_keys(bidInfo['bidUnit2'])
        driver.find_element_by_css_selector("div.el-dialog__body form:nth-of-type(3) [placeholder='单位名称']").send_keys(bidInfo['bidUnit3'])
        driver.find_element_by_css_selector("div.el-dialog__body form:nth-of-type(4) [placeholder='单位名称']").send_keys(bidInfo['bidUnit4'])
        driver.find_element_by_css_selector(".el-select[data-v-6d20b754] [placeholder='请选择']").click()
        driver.find_element_by_xpath("//li[.='分包单位']").click()
        driver.implicitly_wait(3)
        driver.find_element_by_css_selector("div.unit-form-item [placeholder='单位名称']").send_keys(bidInfo['bidUnit5'])
        driver.implicitly_wait(3)
        driver.find_element_by_css_selector("div.confirm-button-actions > .el-button--primary").click()
        time.sleep(0.5)
    # 添加地下室
    for j in range(3):
        basementInfo = {
            'basementName': f'地下室{j+1}',
            'basementBuilding': f'{fake.pyint(min_value=1, max_value=33, step=1)},'
                                f'{fake.pyint(min_value=1, max_value=33, step=1)},'
                                f'{fake.pyint(min_value=1, max_value=33, step=1)},'
                                f'{fake.pyint(min_value=1, max_value=33, step=1)},'
                                f'{fake.pyint(min_value=1, max_value=33, step=1)}',
            'basementNum': '-3',
            'topNum': '0',
            'bottomNum': '0'
        }
        driver.find_element_by_xpath("//span[.='地下室']").click()
        driver.find_element_by_xpath("//button[.='添加地下室']").click()
        driver.find_element_by_css_selector("[placeholder='请选择标段']").click()
        list_data1 = driver.find_elements_by_css_selector(
            "div[x-placement='bottom-start'] .el-scrollbar__view .el-select-dropdown__item")
        time.sleep(0.5)
        list_data1[0].click()
        driver.find_element_by_css_selector("[placeholder='地下室名称']").send_keys(basementInfo['basementName'])
        driver.find_element_by_css_selector("[placeholder='地下室楼栋号']").send_keys(basementInfo['basementBuilding'])
        driver.find_element_by_css_selector("[placeholder='地下室楼层']").send_keys(basementInfo['basementNum'])
        driver.find_element_by_css_selector("[placeholder='顶层编号']").send_keys(basementInfo['topNum'])
        driver.find_element_by_css_selector("[placeholder='底层编号']").send_keys(basementInfo['bottomNum'])
        driver.find_element_by_css_selector("div.confirm-button-actions > .el-button--primary").click()
        time.sleep(0.5)
    #  添加楼栋
    for h in range(3):
        buildingInfo = {
            'buildingNum': f'{fake.pyint(min_value=1, max_value=33, step=1)}',
            'allFloor': f'{fake.pyint(min_value=1, max_value=33, step=1)}',
            'floor1': f'{fake.pyint(min_value=1, max_value=33, step=1)}',
            'floor2': f'{fake.pyint(min_value=1, max_value=33, step=1)}',
            'number1': f'{fake.pyint(min_value=1, max_value=33, step=1)}',
            'number2': f'{fake.pyint(min_value=1, max_value=33, step=1)}',
            'allRoom': f'{fake.pyint(min_value=1, max_value=400, step=1)}',
            'room1': f'{fake.pyint(min_value=1, max_value=200, step=1)}',
            'room2': f'{fake.pyint(min_value=1, max_value=200, step=1)}',
            'topNum': '0',
            'bottomNum': '0'
        }
        driver.find_element_by_css_selector("div.choice-tab > span:nth-of-type(3)").click()
        driver.find_element_by_css_selector("div#addbid > .el-row > button:nth-of-type(2) > span").click()
        driver.find_element_by_css_selector("[placeholder='请选择标段']").click()
        list_data2 = driver.find_elements_by_css_selector("div[x-placement='bottom-start'] .el-scrollbar__view .el-select-dropdown__item")
        time.sleep(0.5)
        list_data2[0].click()
        driver.find_element_by_css_selector("[placeholder='楼栋号']").send_keys(buildingInfo['buildingNum'])
        driver.find_element_by_css_selector("[placeholder='总层数']").send_keys(buildingInfo['allFloor'])
        driver.find_element_by_css_selector("[placeholder='标准层数']").send_keys(buildingInfo['floor1'])
        driver.find_element_by_css_selector("[placeholder='非标准层数']").send_keys(buildingInfo['floor2'])
        driver.find_element_by_css_selector("[placeholder='标准层层号']").send_keys(buildingInfo['number1'])
        driver.find_element_by_css_selector("[placeholder='非标准层层号']").send_keys(buildingInfo['number2'])
        driver.find_element_by_css_selector("[placeholder='总房间数']").send_keys(buildingInfo['allRoom'])
        driver.find_element_by_css_selector("[placeholder='标准层房数']").send_keys(buildingInfo['room1'])
        driver.find_element_by_css_selector("[placeholder='非标准层房数']").send_keys(buildingInfo['room2'])
        driver.find_element_by_css_selector("[placeholder='顶层编号']").send_keys(buildingInfo['topNum'])
        driver.find_element_by_css_selector("[placeholder='底层编号']").send_keys(buildingInfo['bottomNum'])
        driver.find_element_by_css_selector("div.confirm-button-actions > .el-button--primary").click()
        time.sleep(1)
    driver.find_element_by_xpath("//button[.='返回']").click()

driver.quit()
