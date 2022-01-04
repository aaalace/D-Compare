from urllib import request


def check_connection():
    try:
        request.urlopen('http://google.com')
        return True
    except:
        print('False')
        return False