import requests
from datetime import datetime

usr = input("Enter username: ")
passw = input("Enter password: ")


link = 'https://www.instagram.com/accounts/login/'
login_url = 'https://www.instagram.com/accounts/login/ajax/'

time = int(datetime.now().timestamp())

payload = {
    'username': usr,
    'enc_password': '#PWD_INSTAGRAM_BROWSER:0:{time}:' + passw,
    'queryParams': {},
    'optIntoOneTap': 'false'
}

with requests.Session() as s:
    r = s.get(link)
    r = s.post(login_url,data=payload,headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://www.instagram.com/accounts/login/",
        "x-csrftoken":'wbLOjknpi6SZyrdmZSzZN2lAb64q6uLr'
    })
    cookie = s.cookies
    cookies_dictionary = cookie.get_dict()
    print('session id --> ' + cookies_dictionary['sessionid'])
    print('status code --> ' + r.status_code)
    input()