from io import StringIO

f=StringIO()
print(f.write('hello'))
print(f.write(','))
f.write('world!')

print(f.getvalue())

f2=StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s=f2.readline()
    if s=='':
        break
    print(s.strip())
