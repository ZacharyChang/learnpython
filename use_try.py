try:
    print('try...')
    r=10/0
    print('result:',r)
except ZeroDivisionError as e:
    print('except:',e)
finally:
    print('finally...')
print('End')

try:
    print('try...')
    r2=10/3
    print('result:',r2)
except ZeroDivisionError as e:
    print('except:',e)
finally:
    print('finally...')
print('End')

try:
    r3=10/int('a')
    print('result:',r3)
except ValueError as e:
    print('ValueError:',e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:',e)
else:
    print('no error')
finally:
    print('finally...')
print('End')


def foo(s):
    return 10/int(s)

def bar(s):
    return foo(s)*2

def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:',e)
    finally:
        print('finally...')

main()
