import CF

if  __name__ == '__main__':
    d1 = CF.CF(r'D:\0COCO\本科\大二下学期\2017新东方计算机')
    vType = ['.mp4', '.avi', '.vob', '.mkv', '.VOB', '.flv', '.wmv', '.mov', '.rmvb', '.ts']
    d1.MoveOldFiles(vType, Str = '_coco56')
    #d1.MoveOldFiles(Str = '_coco56')
    pass