from FN import FN
import datetime
import os
import shutil

class CF:
    '''
    本类用于操作文件
    '''
    def __init__(self, workDir):
        self.workDir = workDir
        self.log = []
        self.GSTime = datetime.datetime.now()
        self.FNIns = FN(self.workDir)
        self.FNIns.analyzeExtensions()
        self.name = ''
    
    def DelOldFiles(self, Type, Str = ''):
        self.__Start('删除文件')
        c = 1
        for i in self.FNIns.filesName:
            analyze = self.FNIns.analyzeFN(i)
            if(analyze[2] in Type and not Str == '' and analyze[1].find(Str)==-1):
                LSTime = datetime.datetime.now()
                print(c, i)
                os.remove(i)
                LETime = datetime.datetime.now()
                self.log.append(str(c) + '  已删除：' + i + '\n' + '此子任务开始于：' + str(LSTime) + '    总历时：' + str(LETime - LSTime))
                c += 1
        self.__Stop()

    def MoveOldFiles(self, Type, Str = ''):
        self.__Start('移动文件')
        c = 1
        time = str(datetime.datetime.now())
        time = time.replace(':','：')
        move_d = self.workDir
        move_di = move_d + '\\000move_dir' + time
        if not os.path.exists(move_di):
            os.mkdir(move_di)
        for i in self.FNIns.filesName:
            analyze = self.FNIns.analyzeFN(i)
            if(analyze[2] in Type and not Str == '' and analyze[1].find(Str)==-1):
                move_dir = analyze[0].replace(move_d, '', 1)
                move_dir = move_di + move_dir
                if not os.path.exists(move_dir):
                    os.makedirs(move_dir)
                LSTime = datetime.datetime.now()
                print(c, i)
                shutil.move(i, move_dir)
                LETime = datetime.datetime.now()
                self.log.append(str(c) + '  已移动：' + i + '-->' + move_dir + '\n' + '此子任务开始于：' + str(LSTime) + '    总历时：' + str(LETime - LSTime))
                c += 1
        self.__Stop()

    def MoveOldFilesWithList(self, OldFiles):
        self.__Start('移动文件')
        c = 1
        time = str(datetime.datetime.now())
        time = time.replace(':','：')
        move_dir = os.path.dirname(self.workDir) + '\\000move_dir' + time
        if not os.path.exists(move_dir):
            os.mkdir(move_dir)
        for i in OldFiles:
            LSTime = datetime.datetime.now()
            print(c, i)
            shutil.move(i, move_dir)
            LETime = datetime.datetime.now()
            self.log.append(str(c) + '  已移动：' + i + '-->' + move_dir + '\n' + '此子任务开始于：' + str(LSTime) + '    总历时：' + str(LETime - LSTime))
            c += 1
        self.__Stop()

    def __Start(self, name):
        self.name = name
        self.log.append(self.name + '任务开始于：' + str(self.GSTime))

    def __Stop(self):
        print(self.FNIns.filesNum)

        self.GETime = datetime.datetime.now()
        print(self.GETime - self.GSTime)
        self.log.append(self.name + '任务结束于' + str(self.GETime) + '    总历时:' + str(self.GETime-self.GSTime))

        time = str(datetime.datetime.now())
        time = time.replace(':','：')
        logs_dir = os.getcwd() + '\\logs'
        if not os.path.exists(logs_dir):
            os.mkdir(logs_dir)
        logf = logs_dir + '\\' + self.name + '_log_' + time +'.txt'
        with open(logf, 'w', encoding = 'utf-8') as f:
            for i in self.log:
                f.write(i + '\n')
            f.close()
        self.log = []
        print(self.name + '的日志文件已保存在：' + logf)