from configparser import ConfigParser
import os


class MyConfigParser(ConfigParser):
    # 重写 Configparser 中的 optionxform 函数，解决 .ini 文件中的 键option 自动转为小写的问题
    def __init__(self, defaults=None):
        ConfigParser.__init__(self, defaults=defaults)

    def optionxform(self, optionStr):
        return optionStr


class ReadFileData(object):

    def __init__(self):
        self.BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))  # 获取当前项目的绝对路径

    def load_ini(self, ini_file_name='config.ini'):
        file_path = os.path.join(self.BASE_PATH, 'config', ini_file_name)
        config = MyConfigParser()
        config.read(file_path, encoding="UTF-8")
        data_ini = config._sections
        # print("读到数据 ==>>  {} ".format(data))
        return data_ini


data = ReadFileData()

if __name__ == '__main__':
    print(data.load_ini())