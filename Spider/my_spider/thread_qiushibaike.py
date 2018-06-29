import requests
import json
from threading import Thread
from queue import Queue
from lxml import etree

class QiuShiBaiKe:
    '''
    多线程爬虫
    '''

    def __init__(self):
        self.url_temp = "https://www.qiushibaike.com/8hr/page/{}/"
        self.headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"}
        self.url_queue = Queue()
        self.html_queue = Queue()
        self.content_queue = Queue()

    def get_url_list(self):
        for i in range(1, 14):
            self.url_queue.put(self.url_temp.format(i))

    def parser_url(self):
        while True:
            url = self.url_queue.get()
            print(url)
            response = requests.get(url, headers=self.headers)
            self.html_queue.put(response.content.decode())
            self.url_queue.task_done()

    def get_content_list(self):
        while True:
            html_str = self.html_queue.get()
            html = etree.HTML(html_str)
            div_list = html.xpath("//div[@id='content-left']/div")
            content_list = []
            for div in div_list:
                item = {}
                item["content"] = div.xpath(".//div[@class='content']/span/text()")
                item["content"] = [i.replace("\n", "") for i in item["content"]]
                item["author_age"] = div.xpath(".//div[contains(@class,'articleGender')]/text()")
                item["author_age"] = item["author_age"][0] if len(item["author_age"]) > 0 else None
                item["author_gender"] = div.xpath(".//div[contains(@class,'articleGender')]/@class")
                item["author_gender"] = item["author_gender"][0].split(" ")[-1].replace("Icon", "") if len(
                    item["author_gender"]) > 0 else None
                item["stats_vote"] = div.xpath(".//span[@class='stats-vote']/i/text()")
                item["stats_vote"] = item["stats_vote"][0] if len(item["stats_vote"]) > 0 else None
                item["content_img"] = div.xpath(".//div[@class='thumb']/a/img/@src")[0] if len(
                    div.xpath(".//div[@class='thumb']/a/img/@src")) > 0 else None
                item["author_img"] = div.xpath(".//div[@class='author clearfix']//img/@src")
                item["author_img"] = "https:" + item["author_img"][0] if len(item["author_img"]) > 0 else None
                content_list.append(item)
            self.content_queue.put(content_list)
            self.html_queue.task_done()

    def save_content_list(self):
        while True:
            content_list = self.content_queue.get()
            with open('多线程-糗百', 'a', encoding='gbk') as f:
                f.write(json.dumps(content_list, ensure_ascii=False, indent=2))
            self.content_queue.task_done()

    def run(self):
        thread_list = []
        t_url = Thread(target=self.get_url_list)
        thread_list.append(t_url)
        t_parse = Thread(target=self.parser_url)
        thread_list.append(t_parse)
        t_content = Thread(target=self.get_content_list)
        thread_list.append(t_content)
        t_save_data = Thread(target=self.save_content_list)

        for t in thread_list:
            t.setDaemon(True)
            t.start()

        for q in [self.url_queue, self.html_queue, self.content_queue]:
            q.join()

        print('结束')


if __name__ == '__main__':
    qiushi = QiuShiBaiKe()
    qiushi.run()