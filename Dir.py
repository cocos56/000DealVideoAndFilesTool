import os

class Dir:
    '''
    本类用于操作目录
    '''
    def __init__(self):
        pass
    
    def CFD(self, dir = 'temp'):
        FD = os.path.dirname(os.getcwd())
        t = FD + '\\' + dir
        if(not os.path.exists(t)):
            os.mkdir(t)