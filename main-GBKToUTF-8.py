import FN
import CF
import os

if  __name__ == '__main__':
    wordDir = r'D:\temp\project\01Tests\3-fightPlane\Classes'
    scrEnc = 'utf-8'
    desEnc = 'gbk'
    Type = ['.cpp', '.h', '.lrc']
    fn1 = FN.FN(wordDir)
    fn1.analyzeExtensions()
    c = 1
    error = []
    oldFiles = []
    for i in fn1.filesName:
        t = fn1.analyzeFN(i)
        if t[2] in Type:
            try:
                with open(t[0]+t[1]+t[2], 'r', encoding = scrEnc) as f:
                    text = f.read()
                    fileDir = t[0]+t[1]+t[2]
                    if (fileDir.find('_coco56_GBK_To_UTF-8') == -1):
                        print('c=', c, sep='')
                        print(t)
                        c += 1
                        oldFiles.append(fileDir)
                        newFileDir = t[0]+t[1]+'_coco56_GBK_To_UTF-8'+t[2]
                        if(not os.path.exists(newFileDir)):
                            with open(newFileDir , 'w', encoding = desEnc) as f2:
                                f2.write(text)
            except UnicodeDecodeError:
                 error.append(t)
    cf = CF.CF(wordDir)
    cf.MoveOldFilesWithList(oldFiles)
    print(fn1.filesNum)
    pass