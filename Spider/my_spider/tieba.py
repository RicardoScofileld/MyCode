import requests


class Tieba_spirder():
    def __init__(self, name):
        self.name = name
        self.temp_url = "https://tieba.baidu.com/f?kw=" + self.name + "&ie=utf-8&pn={}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"}

    def get_url_list(self):
        return [self.temp_url.format(i*50) for i in range(10)]

    def parse_url(self, url):
        print(url)
        response = requests.get(url, headers=self.headers)
        return response.content.decode('gbk')

    def save_html(self, html_str, page_num):
        file_path = '{}第{}页'.format(self.name, page_num)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html_str)

    def run(self):
        url_list = self.get_url_list()
        for url in url_list:
            html_str = self.parse_url(url)
            page_num = url_list.index(url) + 1
            self.save_html(html_str, page_num)


if __name__ == '__main__':
    jianhun = Tieba_spirder('jianhun')
    jianhun.run()