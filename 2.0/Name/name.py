from os.path import splitext, basename, dirname, join
from os import rename
from Storer.api import insertToDelStr


def setNewName(newName, path, cnt, exe=False):
    oldFileName, oldFileExName = splitext(basename(path))
    fatherDir = dirname(path)
    oldPath = join(fatherDir, oldFileName + oldFileExName)
    newPath = join(fatherDir, newName + oldFileExName)
    print(cnt, oldPath, '-->', newPath)
    if exe:
        rename(oldPath, newPath)
        insertToDelStr(fatherDir, basename(oldPath), basename(newPath))


