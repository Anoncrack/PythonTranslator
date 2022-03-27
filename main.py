from gettext import translation
import requests

URL_AUTH = 'https://developers.lingvolive.com/api/v1.1/authenticate'
URL_TRANSLATE = 'https://developers.lingvolive.com/api/v1/Minicard'
KEY = 'MzUwZjcwNmYtYTUzMi00YmMzLWJiNWItNjdlMDliNjYzNmVjOmFiZDU2NTczZDRiMDQ0ODhiMWZiMDJhYzI2Mjc5MTFi'
headers_auth = {'Authorization': 'Basic ' + KEY}
auth = requests.post(URL_AUTH, headers=headers_auth)
if auth.status_code == 200:
    token = auth.text

    while True:
        print('Английский > Русский')
        word = input('Введите слово: ')
        if word:
            headers_translate = {
                'Authorization': 'Bearer ' + token
            }
            params = {
                'text': word,
                'srcLang': 1033,
                'dstLang': 1049

            }
            r = requests.get (URL_TRANSLATE, headers=headers_translate, params=params)
            res = r.json()
            try:
                print('Перевод:', res['Translation']['Translation'])
            except:
                print('Не найдено')

else:
    print('Ошибка Аунтификации')
