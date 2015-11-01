a='1234567'
print(a)
print(int(a))
print(int(a,base=8))
print(int(a,16))

import functools
int2=functools.partial(int,base=2)
print(int2('1000000'))
