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
    #ins.Transcode(aimedFormat='.ts', dealOldFilesMode=1)
    ins.Transcode(aimedFormat='.mp4', dealOldFilesMode=1)
    
    os.chdir('..')
    os.rmdir(cwd2)
    pass