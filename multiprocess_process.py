import os

print('Process (%s) start...' %os.getpid())

#the code below can't work on windows
'''
pid=os.fork()
if pid == 0:
    print('child process (%s) : parent is %s.' %(os.getpid(),os.getppid()))
else:
    print('%s create a child process (%s).' %(os.getpid(),pid())
'''

from multiprocessing import Process

#子进程执行代码
#在win平台下的IDLE里执行有问题！
def run_proc(name):
    print('Run child process %s (%s)...' %(name,os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' %os.getpid())
    p=Process(target=run_proc,args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')
