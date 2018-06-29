import os
import requests
import json
import random
from lxml import etree
from ip_spider import ProxyIP


class JDSpider(object):
    '''京东spider，输入keyword初始化爬虫，获取该商品的价格，店铺，评论数等信息'''

    def __init__(self, keyword):
        self.temp_url = 'https://search.jd.com/Search?keyword={}&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&bs=1&wq=intel&ev=exbrand_%E8%8B%B1%E7%89%B9%E5%B0%94%EF%BC%88Intel%EF%BC%89%5E&page={}&s=59&click=0'.format(keyword)
        self.temp_url1 = 'https://search.jd.com/s_new.php?keyword={}&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&bs=1&wq=intel&ev=exbrand_%E8%8B%B1%E7%89%B9%E5%B0%94%EF%BC%88Intel%EF%BC%89%5E&page={}&s=135&scrolling=y&tpl=1_M'.format(keyword)
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
        self.result_list = []

    def parse_url(self, url, proxies):
        print(self.headers)
        response = requests.get(url, headers=self.headers, proxies=proxies)
        return response

    def get_data(self, html_str):
        html = etree.HTML(html_str)
        li_list = html.xpath("//ul[@class='gl-warp clearfix']/li")
        for li in li_list:
            item = {}
            print(li.xpath("./@class"))
            item['p_price'] = ''.join(li.xpath(".//div[@class='p-price']//i/text()"))
            item['p_name'] = ''.join(li.xpath(".//div[@class='p-name p-name-type-2']//em/text()"))
            item['p_shop'] = ''.join(li.xpath(".//a[@class='curr-shop']/text()"))
            item['p_commit'] = ''.join(li.xpath(".//div[@class='p-commit']//a/text()"))
            print(item)
            self.result_list.append(item)

    def ip_clean(self, proxy_ip_list):
        invalid_ip = []
        for ip in proxy_ip_list:
            try:
                response = requests.get('http://www.baidu.com', timeout=3, proxies=ip)
            except:
                invalid_ip.append(ip)
        for ip in invalid_ip:
            proxy_ip_list.remove(ip)
        return proxy_ip_list

    def extract_data(self, html_str):
        html = etree.HTML(html_str)
        li_list = html.xpath('//li')
        for li in li_list:
            item = {}
            print(li.xpath("./@class"))
            item['p_price'] = ''.join(li.xpath(".//div[@class='p-price']//i/text()"))
            item['p_name'] = ''.join(li.xpath(".//div[@class='p-name p-name-type-2']//em/text()"))
            item['p_shop'] = ''.join(li.xpath(".//a[@class='curr-shop']/text()"))
            item['p_commit'] = ''.join(li.xpath(".//div[@class='p-commit']//a/text()"))
            print(item)
            self.result_list.append(item)

    def save_data(self):
        with open('jd.txt', 'w') as f:
            json.dump(self.result_list, f)

    def run(self):
        if not os.path.exists('./proxy_ip'):
            # 爬取代理ip
            proxy_ip = ProxyIP()
            proxy_ip_list = proxy_ip.run()
        with open('./proxy_ip', 'r') as f:
            proxy_ip_list = json.load(f)
            # proxy_ip_list = self.ip_clean(proxy_ip_list)
            # json.dump(proxy_ip_list, f)
        for i in range(1, 89):
            url = self.temp_url.format(2 * i - 1)
            print(url)
            html_str = self.parse_url(url, random.choice(proxy_ip_list))
            self.get_data(html_str.content)
            # 请求动态加载的页面
            self.headers['referer'] = url
            url = self.temp_url1.format(2 * i)
            html_str = self.parse_url(url, random.choice(proxy_ip_list))
            print(html_str)
            self.extract_data(html_str.text)
        # 保存数据
        self.save_data()

if __name__ == '__main__':
    # 输入关键字初始化爬虫
    jd_spider = JDSpider()
    jd_spider.run()
