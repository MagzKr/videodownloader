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


    def m3u8_parser(self, url):
        itemid = None
        if 'egorarslanov' in url:
            itemid = 0
        if 'gyneco' in url:
            itemid = 1
        s = requests.Session()
        data = [{
            'action': 'processXdget',
            'xdgetId': '99945',
            'params[action]': 'login',
            'params[url]': 'https://get.egorarslanov.ru/cms/system/login?required=true',
            'params[email]': 'mid97@mail.ru',
            'params[password]': 'qwerty',
            'params[object_type]': 'cms_page',
            'params[object_id]': '-1',
            'requestTime': '1580323420',
            'requestSimpleSign': '0ba52fcf1bee0dace58a5df2c04ff5cc',
        }, {'action': 'processXdget',
            'xdgetId': 99945,
            'params[action]': 'login',
            'params[url]': 'https://gyneco.getcourse.ru/cms/system/login?required=1',
            'params[email]': 'mid97@mail.ru',
            'params[password]': 'qwerty222',
            'params[null]': ' ',
            'params[object_type]': 'cms_page',
            'params[object_id]': -1,
            'requestTime': 1581004611,
            'requestSimpleSign': '6416801119cdcd74c81fdaf056cfdd32'}]
        s.get(data[itemid]['params[url]'])
        s.post(data[itemid]['params[url]'], data[itemid])
        r = s.get(url)
        for i in r.text.splitlines():
            if itemid == 0 and '/player/' in i:
                r = s.get(i[i.find('https'): i.find('"></iframe>')])
                for i in r.text.splitlines():
                    if 'data-master' in i:
                        r = s.get(i[i.find('https'): -1])
                r = r.text.splitlines()
                self.m3u8 = requests.get(r[-1])
                return self.m3u8 # если курс Арсланова
            if itemid == 1 and 'player.vimeo.com' in i:
                r = s.get('https://' + i[i.find('player'): i.find('></iframe>')])
                for elem in r.text.split('"'):
                    if '.mp4' in elem:
                        return elem


    def mp4_downloader(self, url , path):
        with open(path, "wb") as f:
            response = requests.get(url, stream=True)
            total_length = response.headers.get('content-length')
            dl = 0
            total_length = int(total_length)
            for data in response.iter_content(chunk_size=4096):
                dl += len(data)
                f.write(data)
                done = int(100 * dl / total_length)
                self.progress_sign.emit(done)

    def run(self):
        self.data = self.m3u8_parser(url=self.mainwindow.lineLink.text())
        if 'mp4' in self.data:
            self.mp4_downloader(self.data, self.mainwindow.SavePath.text())
        else:
            self.segments = self.getSegsNum(self.data)
            self.dumpSegs(self.segments, self.mainwindow.SavePath.text())