class Fib(object):
    def __init__(self):
        self.a,self.b=0,1   #初始化计数器

    def __iter__(self):
        return self     #实例本身就是迭代对象，返回自己

    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a>100000:
            raise StopIteration()
        return self.a   #返回下一个

for n in Fib():
    print(n)
