#error_logging
import logging

def foo(s):
    return 10/int(s)

def bar(s):
    return foo(s)*2

try:
    bar('0')
except Exception as e:
    logging.exception(e)
print('End')
