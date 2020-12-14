from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

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
driver.find_element_by_xpath("//span[.='添加项目']").click()
driver.implicitly_wait(3)
driver.find_element_by_css_selector("[placeholder='请选择所属事业部:']").click()
opt = driver.find_element_by_css_selector("[placeholder='请选择所属事业部:']")
len_opt = len(driver.find_elements_by_css_selector("div[x-placement='bottom-start'] .el-scrollbar__view li"))
# print(len_opt)
i = 0
while len_opt > i:
    i += 1
    if i == len_opt:
        break
    Select(opt).select_by_index(i)
    time.sleep(0.8)

time.sleep(2)
driver.quit()
