import requests
import chardet
from bs4 import BeautifulSoup


def check_links(url):
    try:
        # 发送 HTTP 请求获取页面内容
        response = requests.get(url)
        response.raise_for_status()  # 确保请求成功

        if 'charset' in response.headers.get('content-type', '').lower():
            response.encoding = response.apparent_encoding
        else:
            # 使用 chardet 检测编码
            detected_encoding = chardet.detect(response.content)['encoding']
            response.encoding = detected_encoding if detected_encoding else 'utf-8'

        # 解析页面内容
        soup = BeautifulSoup(response.text, 'lxml')

        # 查找所有链接
        links = soup.find_all('a', href=True)
        hrefs = [link['href'] for link in links]
        print(hrefs)
    except requests.exceptions.RequestException as e:
        print(f"Error accessing {url}: {e}")


check_links("https://www.360proxy.com/zh-tw/")