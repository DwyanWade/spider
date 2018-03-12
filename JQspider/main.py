import url_manager
import html_downloader 
import html_parser
import html_outputer
import data

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
        self.data = data.SpiderData()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            new_url = self.urls.get_new_url()
            print('craw %d: %s' % (count, new_url))
            html_count = self.downloader.download(new_url)
            new_urls, new_data = self.parser.parse(html_count)
            self.urls.add_new_urls(new_urls)
            self.data.collect_data(new_data)

            if count == 8:
                break
            count = count + 1
        self.data.write_datas()


if __name__ == '__main__':
    root_url = 'https://www.xiangha.com/caipu/89105481.html'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)