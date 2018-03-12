from urllib import request


class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'} 
        response = request.Request(url=url, headers=headers)
        response = request.urlopen(response)

        if response.getcode() != 200:
            return None

        return response.read()
