from CV import CV
import os
import sys
import datetime

if  __name__ == '__main__':
    cwd = r'D:\temp\新建文件夹'
    time = str(datetime.datetime.now())
    time = time.replace(':','：')
    cwd2 = cwd + '\\temp_coco56_' + time
    os.mkdir(cwd2)
    os.chdir(cwd2)
    
    ins = CV()
    os.chdir('..')
    ins.combineTs()

    os.rmdir(cwd2)
    pass