import requests

def visitor(url):
    '''requestes模块初试'''
    url = 'http://' + url
    response = requests.get(url)
    return response.content.decode()


if __name__ == "__main__":
    url = input('请输入域名')
    response_str = visitor(url)
    print(response_str)
