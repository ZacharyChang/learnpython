from wsgiref.simple_server import make_server

def application(enciron,start_response):
    start_response('200 ok',[('Content-Type','text/html')])
    return [b'<h1>Hello,World!</h1>']

# 创建一个server，IP地址为空，端口8000，处理函数是application()
httpd = make_server('',8000,application)
print('Serving Http request on port 8000...')
# 开始监听HTTP请求
httpd.serve_forever()
