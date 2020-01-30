""" download segmented mpeg video (.ts files) from streaming websites """
import requests

OUTNAME = 'video.ts'  # default output file name
LOC = ""  # default save location

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


def dumpSegs(segments, path):
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
            print('Downloaded', '%.2f' % perc, '%')


def m3u8_parser():
    s = requests.Session()
    data = {
            'action':'processXdget',
            'xdgetId':'99945',
            'params[action]': 'login',
            'params[url]':	'https://get.egorarslanov.ru/cms/system/login?required=true',
            'params[email]':	'mid97@mail.ru',
            'params[password]':	'qwerty',
            'params[object_type]':	'cms_page',
            'params[object_id]':	'-1',
            'requestTime':	'1580323420',
            'requestSimpleSign':	'0ba52fcf1bee0dace58a5df2c04ff5cc',
    }
    url = 'https://get.egorarslanov.ru/cms/system/login?required=true'
    s.get(url)
    s.post('https://get.egorarslanov.ru/cms/system/login?required=true', data)
    r = s.get('https://get.egorarslanov.ru/pl/teach/control/lesson/view?id=98044439&editMode=0')
    for i in r.text.splitlines():
        if '/player/' in i:
            r = s.get(i[i.find('https'): i.find('"></iframe>')])

    for i in r.text.splitlines():
        if 'data-master' in i:
            r = s.get(i[i.find('https'): -1])
    r = r.text.splitlines()
    m3u8 = requests.get(r[-1])
    return m3u8


if __name__ == "__main__":
    DEST = LOC + OUTNAME
    m3u8 = m3u8_parser()
    segments = getSegsNum(m3u8)
    dumpSegs(segments, DEST)