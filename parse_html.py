import requests
def m3u8_parser(url, email, password):
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
    m3u8_url = r[-1]
    return m3u8_url