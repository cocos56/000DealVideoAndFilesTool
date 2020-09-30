from os import remove
from .path import getFiles
from os.path import splitext


def removeFiles(files):
    for f in files:
        try:
            remove(f)
            print('删除', f)
        except Exception as e:
            print(e)


def getFilesType():
    cnt = 0
    extensions = {'sum': cnt}
    for file in getFiles(True):
        cnt += 1
        e = splitext(file)[1]
        if e not in extensions:
            extensions.update({e: 1})
        else:
            extensions.update({e: extensions[e] + 1})
    extensions.update({'sum': cnt})
    print(extensions)


