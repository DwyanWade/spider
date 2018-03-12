import re
from urllib import request
from bs4 import BeautifulSoup


class Spider():
    url = 'https://www.xiangha.com/caipu/89799111.html'
    root_pattern = '<div class="video-info">([\s\S]*?)</div>'
    name_pattern = '</i>([\s\S]*?)</span>'
    number_pattern = '<span class="video-number">([\s\S]*?)</span>'
    img_pattern = 'src="([\s\S]*?)"/><span class="good"></span>'
    img_step_pattern = 'src="([\s\S]*?)"'

    def __fetch_content(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        req = request.Request(url=Spider.url, headers=headers)
        r = request.urlopen(req)
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        return htmls

    def go(self):
        htmls = self.__fetch_content()
        soup = BeautifulSoup(htmls, "html.parser")
        ctns = soup.find_all('td', width="50%")
        for ctn in ctns:
            result = ctn.find('div', class_="cell")
            result.span.extract()
            result = result.get_text()
            result = re.sub('相克食物', '', result)
            print(result)

    def go1(self):
        htmls = self.__fetch_content()
        soup = BeautifulSoup(htmls, "html.parser")
        ctns = soup.find('div', class_="pic")
        ctns = str(ctns)
        ctn = re.findall(Spider.img_pattern, ctns)
        print(ctn[0])

    def go2(self):
        htmls = self.__fetch_content()
        soup = BeautifulSoup(htmls, "html.parser")
        ctns = soup.find_all('li', class_="list2")
        for ctn in ctns:
            obj = {}
            obj['index'] = ctn.find('span').get_text()
            ctn.span.extract()
            obj['step'] = ctn.find('p').get_text()
            step_img_path = re.findall(Spider.img_step_pattern, str(ctn))
            obj['img'] = step_img_path[0]
            print(obj)


spider = Spider()
spider.go1()
