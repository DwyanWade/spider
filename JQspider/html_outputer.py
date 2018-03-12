class HtmlOutputer(object):

    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)
    
    def output_html(self):
        font = open('output.html', 'w', encoding='utf-8')

        font.write("<html>")
        font.write("<body>")
        font.write("<table>")

        for data in self.datas:
            font.write("<tr>")
            font.write("<td>%s</td>" % data['title'])
            font.write("<td>%s</td>" % data['like'])
            font.write("</tr>")
        font.write("</table>")
        font.write("</body>")
        font.write("</html>")

        font.close()