import requests
from lxml import etree
import json
import time


class ProxyIP():
    '''代理ip爬取'''

    def __init__(self):
        self.temp_url = 'https://www.kuaidaili.com/free/inha/{}'
        self.hearders = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

    def parse_url(self, url):  # 解析url
        response = requests.get(url, headers=self.hearders)
        return response.content

    def get_data(self, content):
        html = etree.HTML(content)
        tr_list = html.xpath('//tbody/tr')
        proxy_ip_list = []
        for tr in tr_list:
            item = {}
            ip = tr.xpath('./td[1]/text()')[0]
            port = tr.xpath('./td[2]/text()')[0]
            ip_type = tr.xpath('./td[4]/text()')[0]
            item[ip_type] = ip_type + '://' + ip + ':' + port
            proxy_ip_list.append(item)
        return proxy_ip_list

    def data_clean(self, proxy_ip_list):
        invalid_ip = []
        for ip in proxy_ip_list:
            try:
                response = requests.get('http://www.baidu.com', timeout=3, proxies=ip)
            except Exception as e:
                invalid_ip.append(ip)
        for ip in invalid_ip:
            proxy_ip_list.remove(ip)
        return proxy_ip_list

    def save_data(self, proxy_ip_list):
        with open('proxy_ip', 'w') as f:
            json.dump(proxy_ip_list, f)

    def run(self):
        # 生成url列表
        url_list = []
        for i in range(1, 10):
            url_list.append(self.temp_url.format(i))

        # 遍历列表发送请求
        proxy_ip_list = []
        for url in url_list:
            # 发送请求
            print(url)
            # time.sleep(2)
            content = self.parse_url(url)
            # 提取数据
            ip_list = self.get_data(content)
            proxy_ip_list.extend(ip_list)
        print('开始清除无效ip')
        print(len(proxy_ip_list))
        proxy_ip_list = self.data_clean(proxy_ip_list)
        print('开始保存数据')
        self.save_data(proxy_ip_list)
        return proxy_ip_list

if __name__ == '__main__':
    ip_spider = ProxyIP()
    ip_spider.run()
