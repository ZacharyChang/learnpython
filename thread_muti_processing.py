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
