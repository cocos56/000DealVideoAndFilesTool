import os
import re
import shutil

def getFileName(s):
    l = len(s) - 1
    while(not s[l] == '\\'):
        l -= 1
    return s[l+1:]

log_file = os.getcwd() + '\\logs\\' '移动文件_log_2018-11-18 22：51：00.278361.txt'

fp = open(log_file, 'r', encoding='utf-8')
pattern = '已移动：(.+?)-->(.+)'
reg = re.compile(pattern)
line = fp.readline()
while(line):
    #print(line)
    results = reg.findall(line)
    if(not results == []):
        srcFile = results[0][1] + '\\' + getFileName(results[0][0])
        destFile = results[0][0]
        if(os.path.exists(srcFile)):
            print(results)
            print(srcFile)
            print(destFile)
            shutil.move(srcFile,destFile)
    line = fp.readline()