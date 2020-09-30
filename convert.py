# -*- coding:utf-8 -*-
__author__ = 'coco56'
 
import os,sys
import chardet
import FN
 
def convert( filename, in_enc = "GBK", out_enc="UTF8" ):
    try:
        print("convert " + filename)
        content = open(filename).read()
        result = chardet.detect(content)#通过chardet.detect获取当前文件的编码格式串，返回类型为字典类型
        coding = result.get('encoding')#获取encoding的值[编码格式]
        if coding != 'utf-8':#文件格式如果不是utf-8的时候，才进行转码
            print(coding + "to utf-8!")
            new_content = content.decode(in_enc).encode(out_enc)
            open(filename, 'w').write(new_content)
            print(" done")
        else:
            print(coding)
    except IOError:
    # except:
        print("Error: 没有找到文件或读取文件失败")
 
 
def explore(dir):
    for root, dirs, files in os.walk(dir):
        for file in files:
            path = os.path.join(root, file)
            #print(path)
            convert(path)
 
def main():
    fn1 = FN.FN()
    fn1.analyzeExtensions()
    print(fn1.filesName)
    print(fn1.filesNum)
    print(1)
    print(2)

 
if __name__ == "__main__":
    main()