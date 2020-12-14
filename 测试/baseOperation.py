from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.baidu.com")
page = driver.page_source
print(page)
time.sleep(1)
driver.get("https://www.bilibili.com")
time.sleep(1)
driver.back()
driver.get_screenshot_as_file("E:\\测试\\测试.png")
driver.refresh()
time.sleep(1)
driver.find_element_by_link_text("贴吧").click()
driver.back()
driver.find_element_by_partial_link_text("贴").click()
driver.forward()
driver.get_screenshot_as_file("E:\\测试\\002.png")
time.sleep(1)
driver.quit()


class AddProject(object):
    """
    添加项目信息（地下室楼栋参建单位）
    """

    def __init__(self, url):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(url)


if __name__ == '__main__':
    adder = AddProject('http://manage.supervisor.dev.hfhksoft.com/')
