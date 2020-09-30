import CV

if __name__ == '__main__':
    d = r'H:\度盘\Unity 1127 如何制作塔防游戏（基于Unity5.5）'
    cv1 = CV.CV(workDir=d, sleepTime=1)
    cv1.cutV(11, 0, dealOldFilesMode=0)
    print(cv1.FNIns.filesNum)
