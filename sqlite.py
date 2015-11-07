import sqlite3
#连接到SQLite数据库，文件为test.db
#如果文件不存在则在当前目录创建
conn=sqlite3.connect('test.db')
#执行建表及插入操作
cursor=conn.cursor()
#cursor.execute('create table user (id varchar(20) primary key,name varchar(20))')
#cursor.execute('insert into user (id,name) values(\'1\',\'Micheal\')')
print(cursor.rowcount)
cursor.close()
conn.commit()
conn.close()

#查询记录
conn=sqlite3.connect('test.db')
cursor=conn.cursor()
cursor.execute('select * from user')
values=cursor.fetchall()
print(values)
cursor.close()
conn.close()
