from gettext import translation
import requests
import itertools

URL_AUTH = 'https://developers.lingvolive.com/api/v1.1/authenticate'
URL_TRANSLATE = 'https://developers.lingvolive.com/api/v1/Minicard'
KEY = 'MzUwZjcwNmYtYTUzMi00YmMzLWJiNWItNjdlMDliNjYzNmVjOmFiZDU2NTczZDRiMDQ0ODhiMWZiMDJhYzI2Mjc5MTFi'
headers_auth = {'Authorization': 'Basic ' + KEY}
auth = requests.post(URL_AUTH, headers=headers_auth)
langtoggle = itertools.cycle(['rus', 'eng']).__next__
enval = 1033
ruval = 1049
srcLangVal = enval
dstLangVal = ruval
engstroke = 'ENGLISH > RUSSIAN'
russtroke = 'RUSSIAN > ENGLISH'
lstroke = engstroke
enru = 'Английский > Русский'
ruen = 'Русский > Английский'

    



if auth.status_code == 200:
    token = auth.text

while True:
    print('Чтобы поменять язык - введите !')
    print(lstroke)
    word = input('Введите слово: ')
    if word == '!':
        print('Язык изменен')
        toggled = langtoggle()
        if toggled == 'eng':
            lstroke  = engstroke
            srcLangVal = enval
            dstLangVal = ruval
        if toggled == 'rus':
            lstroke = russtroke
            srcLangVal = ruval
            dstLangVal = enval
        
    if word:
        headers_translate = {
            'Authorization': 'Bearer ' + token
        }
        params = {
            'text': word,
            'srcLang': srcLangVal,
            'dstLang': dstLangVal

        }
        r = requests.get (URL_TRANSLATE, headers=headers_translate, params=params)
        res = r.json()
        try:
            print('-----------------')
            print('Перевод:', res['Translation']['Translation'])
            print('-----------------')
        except:
            if word == '!':
                print()
            else:
                print('Не найдено')

        # else:
        #     print('Ошибка Аунтификации')