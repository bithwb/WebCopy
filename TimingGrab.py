# -*- coding: gb2312 -*-
import time, os, sched 
    
# ��һ������ȷ�������ʱ�䣬���ش�ĳ���ض���ʱ�䵽���ھ��������� 
# �ڶ���������ĳ����Ϊ�ķ�ʽ����ʱ�� 
schedule = sched.scheduler(time.time, time.sleep) 
csd = "Grab.py"
def perform_command(csd, inc): 
    # ����1��Сʱ����ٴ������Լ�������������
    inc = 3600
    schedule.enter(inc, 0, perform_command, (csd, inc)) 
    os.system(csd) 
        
def timming_exe(csd, inc = 60): 
    # enter��������ĳ�¼��ķ���ʱ�䣬���������n�뿪ʼ����
    schedule.enter(inc, 0, perform_command, (csd, inc)) 
    # �������У�ֱ���ƻ�ʱ����б�ɿ�Ϊֹ 
    schedule.run() 
        
    
print("Grab Start!") 
timming_exe(csd, 0)
