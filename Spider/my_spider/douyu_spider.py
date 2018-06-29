import requests
from lxml import etree
import json


class DouYuSpider:
    """
    爬取斗鱼所有分类的房间号
    """

    def __init__(self):
        self.start_url = 'https://www.douyu.com/directory'
        self.type_temp = 'https://www.douyu.com/gapi/rkc/directory/{}/{}'
        self.room_temp = 'https://www.douyu.com/{}'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

    def parse_url(self, url):  # 解析url
        response = requests.get(url, headers=self.headers)
        return response.content

    def get_type_list(self, html_str):
        html = etree.HTML(html_str)
        li_list = html.xpath('//ul[@class="clearfix"]/li')
        type_url_list = []
        for li in li_list:
            item = {}
            item['url'] = li.xpath("./a/@href")
            item['data_rk'] = li.xpath('./a/@data-rk')
            item['title'] = li.xpath('./a/@title')
            type_url_list.append(item)
        return type_url_list

    def run(self):
        # 请求初始url地址，获取页面数据
        html_str = self.parse_url(self.start_url)
        # 获取主播分类列表
        type_list = self.get_type_list(html_str)
        for type in type_list:
            # 获取这个类型有几页数据
            json_str = self.parse_url(self.type_temp.format(type['data_rk'][0], '1')).decode()
            page_num = json.loads(json_str)['data']['pgcnt']
            for i in range(1, page_num + 1):
                json_str = self.parse_url(self.type_temp.format(type['data_rk'][0], i)).decode()
                room_list = json.loads(json_str)['data']['rl']
                for room in room_list:
                    print('游戏种类:{}'.format(type['title']), '主播:{}'.format(room['nn']), '房间名:{}'.format(room['rn']),
                          '房间地址:{}'.format(self.room_temp.format(room['url'])))


if __name__ == '__main__':
    douyu = DouYuSpider()
    douyu.run()
