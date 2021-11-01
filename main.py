import sys
import os


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    os.system('python utils/login_util.py')
    sys.excepthook = except_hook