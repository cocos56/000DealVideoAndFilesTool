from os import walk
from os.path import join
from Config.api import workDirs

files = []
dirs = []


def init():
    files.clear()
    dirs.clear()
    for workDir in workDirs:
        for root, ds, fs in walk(workDir):
            for i in fs:
                temp = join(root, i)
                files.append(temp)
            for i in ds:
                temp = join(root, i)
                dirs.append(temp)


def getFiles(initFlag=True):
    if initFlag:
        init()
    return files


def getDirs(initFlag=True):
    if initFlag:
        init()
    return dirs
