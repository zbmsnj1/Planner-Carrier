# task_worker.py
 
import os 
import queue
import time, sys, queue
 
from multiprocessing.managers import BaseManager

domain = '../../../benchmarks/acrobatics/domain.pddl'

prob= [
'../../../benchmarks/acrobatics/p01.pddl',
'../../../benchmarks/acrobatics/p02.pddl',
'../../../benchmarks/acrobatics/p03.pddl',
'../../../benchmarks/acrobatics/p04.pddl',
'../../../benchmarks/acrobatics/p05.pddl',
'../../../benchmarks/acrobatics/p06.pddl',
'../../../benchmarks/acrobatics/p07.pddl',
'../../../benchmarks/acrobatics/p08.pddl',
'../../../benchmarks/elevators/p09.pddl',
'../../../benchmarks/elevators/p10.pddl',
'../../../benchmarks/elevators/p11.pddl',
'../../../benchmarks/elevators/p12.pddl',
'../../../benchmarks/elevators/p13.pddl',
'../../../benchmarks/elevators/p14.pddl',
'../../../benchmarks/elevators/p15.pddl'] 
 
# 创建类似的QueueManager:
 
class QueueManager(BaseManager):
 
    pass
 
# 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
 
QueueManager.register('get_task_queue')
 
QueueManager.register('get_result_queue')
 
# 连接到服务器，也就是运行task_master.py的机器:
 
server_addr = '192.168.232.129'
 
print('Connect to server %s...' % server_addr)
 
# 端口和验证码注意保持与task_master.py设置的完全一致:
 
m = QueueManager(address=(server_addr, 2001), authkey=b'abc')
 
# 从网络连接:
 
m.connect()
 
# 获取Queue的对象:
 
task = m.get_task_queue()
 
result = m.get_result_queue()
 

def basic_func(doma, prob):
    os.system('./prp '+doma+' '+prob+' --dump-policy 2') 
    
os.chdir('../Experiment/PRP/src/') 
# 从task队列取任务,并把结果写入result队列:
 
for i in range(100):
 
    try:
 
        n = task.get(timeout=1)
        n = basic_func(i,i)

 
        time.sleep(1)
 
        result.put(n)
 
    except Queue.Empty:
 
        print('task queue is empty.')
 
# 处理结束:
 
print('worker exit.')
