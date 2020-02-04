""" download segmented mpeg video (.ts files) from streaming websites """
import requests


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": '',
    "DNT": "1",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache"
}


def getSegsNum(m3):
    """ figure out how many segments there are using the m3u8 file """
    lines = m3.text.split('\n')
    segs = []
    for line in lines:
        if '.ts' in line:
            segs.append(line)
    return segs


def dumpSegs(segments, path, window):
    """ downlaod and combine the .ts files
    given the first seg's url, the number of segments and
    the destination download path """
    perc = 0
    i = 100 / len(segments)
    for url in segments:
        with open(path, 'ab') as f:
            seg = requests.get(url)
            f.write(seg.content)
            perc += i
            window.insertPlainText('Downloaded'+ '%.2f' % perc + '%')
# + '%.2f' % perc + '%'

def m3u8_parser(url, login = 'mid97@mail.ru' , password = 'qwerty'):
    s = requests.Session()
    login_url = 'https://get.egorarslanov.ru/cms/system/login?required=true'
    data = {
            'action':'processXdget',
            'xdgetId':'99945',
            'params[action]': 'login',
            'params[url]':	login_url,
            'params[email]':	login,
            'params[password]':	password,
            'params[object_type]':	'cms_page',
            'params[object_id]':	'-1',
            'requestTime':	'1580323420',
            'requestSimpleSign':	'0ba52fcf1bee0dace58a5df2c04ff5cc',
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
    m3u8 = requests.get(r[-1])
    return m3u8

def start_download(path, window, url):
    m3u8 = m3u8_parser(url)
    segments = getSegsNum(m3u8)
    dumpSegs(segments, path, window)