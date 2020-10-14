from Storer.api import getFromDelStr, delData
from os import rename
from os.path import exists


class Recover:
    @classmethod
    def delFsStr(cls, timestamp):
        cnt = 0
        for i in getFromDelStr(timestamp):
            cnt += 1
            print(cnt, i[1], '-->', i[0])
            if exists(i[1]):
                rename(i[1], i[0])
                print(True)
            else:
                print(False)
        delData(timestamp)
