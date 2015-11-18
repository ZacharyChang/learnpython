from io import BytesIO

f=BytesIO()
f.write('编码为UTF-8'.encode('utf-8'))
print(f.getvalue())

f2=BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f2.read())
