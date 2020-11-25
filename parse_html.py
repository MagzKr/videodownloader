import requests
from data import params
def m3u8_parser(video_url, email, password):
    params['params[email]'] = 	email
    params['params[password]'] = password
    s = requests.Session()
    login_url = 'https://get.egorarslanov.ru/cms/system/login?required=true'
    s.get(login_url)
    s.post('https://get.egorarslanov.ru/cms/system/login?required=true', params)
    r = s.get(video_url)
    for i in r.text.splitlines():
        if '/player/' in i:
            r = s.get(i[i.find('https'): i.find('"></iframe>')])

    for i in r.text.splitlines():
        if 'data-master' in i:
            r = s.get(i[i.find('https'): -1])
    r = r.text.splitlines()
    m3u8_url = r[-1]
    return m3u8_url