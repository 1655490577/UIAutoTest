import requests
import sys


class BaiduTieBa:
    def __init__(self, name, pn, ):
        self.name = name
        self.url = "http://tieba.baidu.com/f?kw={}&ie=utf-8&pn={}".format(name, pn)
        self.headers = {
            # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"

            # 使用较老版本的请求头，该浏览器不支持js
            "User-Agent": "Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0)"
        }
        self.url_list = [self.url + str(pn * 50) for pn in range(pn)]
        print(self.url_list)

    def get_data(self, url):
        """
        请求数据
        :param url:
        :return:
        """
        response = requests.get(url, headers=self.headers)
        return response.content

    def save_data(self, data, num):
        """
        保存数据
        :param data:
        :param num:
        :return:
        """
        file_name = "E:\\UIAutoTest\\wenjian\\" + self.name + "_" + str(num) + ".html"
        with open(file_name, "wb") as f:
            f.write(data)

    def run(self):
        for url in self.url_list:
            data = self.get_data(url)
            num = self.url_list.index(url)
            self.save_data(data, num)


if __name__ == "__main__":
    # name = sys.argv[1]
    # pn = int(sys.argv[2])
    # baidu = BaiduTieBa('1', 2)
    # baidu.run()
    index = "www.baidu.com".rfind('/')
    print(type(index))
