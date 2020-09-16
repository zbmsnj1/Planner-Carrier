# task_master.py
 
import os
import random, time, queue
 
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
 
# 发送任务的队列:
 
task_queue = queue.Queue()
 
# 接收结果的队列:
 
result_queue = queue.Queue()
 
# 从BaseManager继承的QueueManager:
 
class QueueManager(BaseManager):
 
    pass
 
# 把两个Queue都注册到网络上, callable参数关联了Queue对象:
 
QueueManager.register('get_task_queue', callable=lambda: task_queue)
 
QueueManager.register('get_result_queue', callable=lambda: result_queue)
 
# 绑定端口5000, 设置验证码'abc':
 
manager = QueueManager(address=('', 3001), authkey=b'abc')
 
# 启动Queue:
 
manager.start()
 
# 获得通过网络访问的Queue对象:
 
task = manager.get_task_queue()
 
result = manager.get_result_queue()
 


def basic_func(doma, prob):
    os.system('./prp '+doma+' '+prob+' --dump-policy 2') 
 
# 放几个任务进去:

for i in range(0,8): 
    task.put(i)
 
# 从result队列读取结果:
 
print('Try get results...')
 
for i in range(8):
 
    r = result.get(timeout=100)
 
    print(r)
 
# 关闭:
 
manager.shutdown()
 
print('master exit.')

