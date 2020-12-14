# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get('http://www.baidu.com')
# print(driver.title)
# driver.quit()
#
# import requests
# from bs4 import BeautifulSoup
# import re
#
# url = 'http://www.cntour.cn/'
# req = requests.get(url)
# soup = BeautifulSoup(req.text, 'lxml')
# Data = soup.select('#main>div>div.mtop.firstMod.clearfix>div.centerBox>ul.newsList>li>a')
# for i in Data:
#     print(i.get_text())
#     print(i.get('href'))
#     print(re.findall('\d+', i.get('href')))

# a = ['css', 'testTestTest']
#
#
# def test(style, element):
#     print(style)
#     print(element)
#
#
# test(*a)

from selenium import webdriver
from time import sleep
#
#
driver = webdriver.Chrome()
driver.get('http://supervisor.test.hfhksoft.com/')
driver.find_element_by_css_selector("[placeholder='请输入手机号:']").send_keys('admin')
driver.find_element_by_css_selector("[placeholder='请输入密码']").send_keys('admin')
driver.find_element_by_xpath("//span[.='登录']").click()
# sleep(0.1)
# a = driver.find_element_by_css_selector(".el-message").text
# print(a)
addUsername_loc = "css, form.el-form > .is-error > .el-form-item__content > .el-input > .el-input__inner"
addUserPhone_loc = "css, input[maxlength='11']"
addUserPassword_loc = "css, form.el-form > div:nth-of-type(3) .el-input__inner"
addUserCheckPassword_loc = "css, form.el-form > div:nth-of-type(4) .el-input__inner"
addUserStation_loc = "css, form.el-form > div:nth-of-type(5) [placeholder='请选择']"
addUserState_loc = "css, form.el-form > div:nth-of-type(6) [placeholder='请选择']"
addUserBranch_loc = "css, form.el-form > .is-error [placeholder='请选择']"
addUserCommonSearch_loc = "css, div[x-placement='bottom-start']"
addUserProject_loc = "css, .is-multiple"

sleep(1)
driver.find_element_by_css_selector("li[aria-expanded='true'] div:nth-of-type(1) .el-menu-item").click()
driver.find_element_by_css_selector("button.both-add-style > span").click()
sleep(1)
driver.find_element_by_css_selector("form.el-form > div:nth-of-type(7) [placeholder='请选择']").click()
sleep(1)
driver.find_element_by_xpath("//li[.='事业部二']").click()
