#error
def foo(s):
    return 10/int(s)

def bar(s):
    return foo(s)*2

bar('0')

