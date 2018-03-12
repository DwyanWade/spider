import re
from bs4 import BeautifulSoup


class HtmlParser(object):
    courseId = 188
    img_pattern = 'src="([\s\S]*?)"'
    img_step_pattern = 'src="([\s\S]*?)"'
    skin_pattern = '\d+'

    def _get_new_urls(self, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r"https://www.xiangha.com/caipu/\d+\.html"))
        for link in links:
            new_url = link['href']
            new_urls.add(new_url)
        return new_urls

    def _get_new_data(self, soup):
        res_data = {}
        materialList = []
        methodStepList = []

        res_data['courseId'] = HtmlParser.courseId
        title = soup.find('h2', class_="dish-title")
        res_data['courseTitle'] = title.get_text()
        like_node = soup.find('span', id="j_show_favorite")
        res_data['collection'] = like_node.get_text()
        res_data['type'] = "lazy"

        skin = soup.find('div', class_="info")
        skin = skin.get_text()
        skin = re.search(HtmlParser.skin_pattern, skin)
        res_data['skin'] = int(skin.group())

        imgs = soup.find('div', class_="pic")
        imgs = str(imgs)
        img = re.findall(HtmlParser.img_pattern, imgs)
        res_data['courseImg'] = img[0]

        materials = soup.find_all('td', width="50%")
        for material in materials:
            materialObj = {}
            materialObj['weight'] = material.find('span').get_text()
            raw = material.find('div', class_="cell")
            raw.span.extract()
            raw = raw.get_text()
            raw = re.sub('相克食物', '', raw)
            materialObj['raw'] = raw
            materialList.append(materialObj)

        steps = soup.find_all('li', class_="list2")
        for step in steps:
            methodStepObj = {}
            methodStepObj['index'] = step.find('span').get_text()
            step.span.extract()
            methodStepObj['step'] = step.find('p').get_text()
            step_img_path = re.findall(HtmlParser.img_step_pattern, str(step))
            methodStepObj['pic'] = step_img_path[0]
            methodStepList.append(methodStepObj)

        res_data['materialList'] = materialList
        res_data['methodStep'] = methodStepList
    
        HtmlParser.courseId = HtmlParser.courseId + 1
        return res_data

    def parse(self, html_cont):
        if html_cont is None:
            return
        soup = BeautifulSoup(html_cont, "html.parser")
        new_urls = self._get_new_urls(soup)
        new_data = self._get_new_data(soup)
        return new_urls, new_data


