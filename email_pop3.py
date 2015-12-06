import poplib

# 输入邮件地址，口令和POP3服务器地址
email='287265817@qq.com'
password='wmq13143344zzp'
pop3_server='pop.qq.com'

# 连接到POP3服务器
server=poplib.POP3(pop3_server)
server.set_debuglevel(1)
print(server.getwelcome().decode('utf-8'))

# 身份认证
server.user(email)
server.pass_(password)

# stat()返回邮件数量和占用空间
print('Messages: %s. Size: %s' %server.stat())
# list()返回所有邮件的编号
resp,mails,octets=server.list()
print(mails)

# 获取最近一封邮件，索引号从1开始
index=len(mails)
resp,lines,octets=server.retr(index)

# lines存储了邮件的原始文本的每一行
# 可以获得整个邮件的原始文本
msg_content=b'\r\n'.join(lines).decode('utf-8')
# 稍后解析邮件
msg=Parser().parsestr(msg_content)

# 关闭连接
server.quit()
