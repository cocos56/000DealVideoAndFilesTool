from CV import CV

if  __name__ == '__main__':
    d = r'H:\度盘\siki学院公开课第009期-忍者跑酷 Ninja'
    cv1 = CV(workDir=d, sleepTime=1)
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
    threads = 2
    cv1.dealV(speed, dealOldFilesMode, gpu, threads)
    pass
