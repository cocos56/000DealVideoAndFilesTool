from CV import CV

if  __name__ == '__main__':
    d = r'D:\s\De\度盘\C#项目开发实战入门（光盘资源）\Video'
    cv1 = CV(workDir=d, sleepTime=0)
    # speed = 1
    # speed = 1.1
    # speed = 1.2
    # speed = 1.3
    # speed = 1.4
    # speed = 1.5
    speed = 1.6
    # speed = 1.8
    # speed = 2
    dealOldFilesMode = 0
    gpu = False
    cv1.dealV(speed, dealOldFilesMode, gpu, 8)