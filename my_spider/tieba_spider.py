import requests
from lxml import etree
import json


class Tieba:
    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.start_url = "http://tieba.baidu.com/mo/q----,sz@320_240-1-3---2/m?kw=" + tieba_name + "&pn=0"
        self.headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) \
        AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1'}
        self.part_url = "http://tieba.baidu.com/mo/q----,sz@320_240-1-3---2/"

    def parse_url(self, url):
        print(url)
        response = requests.get(url, headers=self.headers)
        return response.content

    def get_content_list(self, html_str):
        html = etree.HTML(html_str)
        div_list = html.xpath("//div[contains(@class,'i')]")
        content_list = []
        for div in div_list:
            item = {}
            item['href'] = self.part_url + div.xpath("./a/@href")[0] if len(div.xpath("./a/@href")[0]) > 0 else None
            item['title'] = div.xpath("./a/text()")[0] if len(div.xpath("./a/text()")[0]) > 0 else None
            item['img_list'] = self.get_img_list(item['href'], [])
            content_list.append(item)
        next_url = self.part_url + html.xpath("//a[text()='下一页']/@href")[0] if len(
            html.xpath("//a[text()='下一页']/@href")) > 0 else None
        return content_list, next_url

    def get_img_list(self, detail_url, total_image_list):
        detail_html_str = self.parse_url(detail_url)
        detail_html = etree.HTML(detail_html_str)
        img_list = detail_html.xpath("//img[@class='BDE_Image']/@src")
        total_image_list.extend(img_list)
        next_detail_url = detail_html.xpath("//a[text()='下一页']/@href")
        if len(next_detail_url) > 0:
            next_detail_url = self.part_url + next_detail_url[0]
            return self.get_img_list(next_detail_url, total_image_list)
        return total_image_list

    def save_content_list(self, content_list):
        file_path = "{}.txt".format(self.tieba_name)
        with open(file_path, "a", encoding='utf-8') as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False, indent=2))
                f.write("\n")
        print("保存成功")

    def run(self):
        next_url = self.start_url
        while next_url:
            html_str = self.parse_url(next_url)
            content_list, next_url = self.get_content_list(html_str)
            print(content_list)
            self.save_content_list(content_list)


if __name__ == '__main__':
    jianhun = Tieba("剑魂")
    jianhun.run()
