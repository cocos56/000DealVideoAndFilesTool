import os
import time
 

#第一种
print(u'测试开始')
os.system('dir')
os.system('ping 192.168.1.1')
print(u'测试结束')
 
 
#第二种
import  subprocess
 
print(u'测试开始')
subprocess.Popen('dir',shell=True)
subprocess.Popen('ping 192.168.1.1',shell=True)
print(u'测试结束')
