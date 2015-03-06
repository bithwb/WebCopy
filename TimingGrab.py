# -*- coding: gb2312 -*-
import time, os, sched 
    
# 第一个参数确定任务的时间，返回从某个特定的时间到现在经历的秒数 
# 第二个参数以某种人为的方式衡量时间 
schedule = sched.scheduler(time.time, time.sleep) 
csd = "Grab.py"
def perform_command(csd, inc): 
    # 安排1个小时后后再次运行自己，即周期运行
    inc = 3600
    schedule.enter(inc, 0, perform_command, (csd, inc)) 
    os.system(csd) 
        
def timming_exe(csd, inc = 60): 
    # enter用来安排某事件的发生时间，从现在起第n秒开始启动
    schedule.enter(inc, 0, perform_command, (csd, inc)) 
    # 持续运行，直到计划时间队列变成空为止 
    schedule.run() 
        
    
print("Grab Start!") 
timming_exe(csd, 0)
