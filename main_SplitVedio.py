from CV import CV
import os
import sys
import datetime

if  __name__ == '__main__':
    cwd = r'D:\\temp\新建文件夹'
    time = str(datetime.datetime.now())
    time = time.replace(':','：')
    cwd2 = cwd + '\\temp_coco56_' + time
    os.mkdir(cwd2)
    os.chdir(cwd2)

    ins = CV()
    ins.split_OneVedio_Into_MultipleVedios_WithNumber(2)
    
    os.chdir('..')
    os.rmdir(cwd2)
    pass