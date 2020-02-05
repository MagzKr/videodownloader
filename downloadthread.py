from PyQt5.QtCore import QThread, pyqtSignal
import requests

class DownloadingThread(QThread):
    progress_sign = pyqtSignal(int)


    def __init__(self, mainwindow, parent=None):
        super().__init__()
        self.mainwindow = mainwindow


    def getSegsNum(self, m3):
        """ figure out how many segments there are using the m3u8 file """
        lines = m3.text.split('\n')
        self.segs = []
        for line in lines:
            if '.ts' in line:
                self.segs.append(line)
        return self.segs


    def dumpSegs(self, segments, path):
        progress = 0
        """ downlaod and combine the .ts files
        given the first seg's url, the number of segments and
        the destination download path """
        i = 100 / len(segments)
        for url in segments:
            with open(path, 'ab') as f:
                seg = requests.get(url)
                f.write(seg.content)
                progress += i
                self.progress_sign.emit(progress)

    def m3u8_parser(self, url, login='mid97@mail.ru', password='qwerty'):
        s = requests.Session()
        login_url = 'https://get.egorarslanov.ru/cms/system/login?required=true'
        data = {
            'action': 'processXdget',
            'xdgetId': '99945',
            'params[action]': 'login',
            'params[url]': login_url,
            'params[email]': login,
            'params[password]': password,
            'params[object_type]': 'cms_page',
            'params[object_id]': '-1',
            'requestTime': '1580323420',
            'requestSimpleSign': '0ba52fcf1bee0dace58a5df2c04ff5cc',
        }
        s.get(login_url)
        s.post(login_url, data)
        r = s.get(url)
        for i in r.text.splitlines():
            if '/player/' in i:
                r = s.get(i[i.find('https'): i.find('"></iframe>')])

        for i in r.text.splitlines():
            if 'data-master' in i:
                r = s.get(i[i.find('https'): -1])
        r = r.text.splitlines()
        self.m3u8 = requests.get(r[-1])
        return self.m3u8


    def run(self):
        self.m3u8 = self.m3u8_parser(self.mainwindow.lineLink.text())
        self.segments = self.getSegsNum(self.m3u8)
        self.dumpSegs(self.segments, self.mainwindow.SaveWay.text())