from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from common.read_data import data


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.base_url = data.load_ini()['driver']['base_url']
        if driver is None:
            self._driver = webdriver.Chrome()
            self._driver.implicitly_wait(3)
            self._driver.get(self.base_url)
            self._driver.maximize_window()
        else:
            self._driver = driver

    @staticmethod
    def split_locator(locator):
        """
        分解定位表达式，如'css,.username',拆分后返回'css selector'和定位表达式'.username'(class为username的元素)
        :param locator: 定位方法+定位表达式组合字符串，如'css,.username'
        :return: locator_dict[by], value:返回定位方式和定位表达式
        """
        by = locator.split(',')[0]
        value = locator.split(',')[1]
        locator_dict = {
            'id': 'id',
            'name': 'name',
            'class': 'class name',
            'tag': 'tag name',
            'link': 'link text',
            'plink': 'partial link text',
            'xpath': 'xpath',
            'css': 'css selector',
        }
        if by not in locator_dict.keys():
            raise NameError("wrong locator!'id','name','class','tag','link','plink','xpath','css',exp:'id,username'")
        return locator_dict[by], value

    def find_element(self, locator, sec=30):
        by, value = self.split_locator(locator)
        return WebDriverWait(self._driver, sec, 1).until(lambda x: x.find_element(by=by, value=value),
                                                         message='element not found!!!')

    def find_elements(self, locator, sec=30):
        by, value = self.split_locator(locator)
        return WebDriverWait(self._driver, sec, 1).until(lambda x: x.find_elements(by=by, value=value),
                                                         message='element not found!!!')

    def get_pageInfo(self, arr):
        if arr == 'url':
            return self._driver.current_url
        if arr == 'title':
            return self._driver.title
        if arr == 'browser_name':
            return self._driver.name
        if arr == 'page_data':
            return self._driver.page_source

    def close(self):
        self._driver.quit()
