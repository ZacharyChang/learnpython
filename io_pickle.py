import pickle

d=dict(name='Bob',age=20,score=77)
f1=open('dump.txt','wb')
pickle.dump(d,f1)
f1.close()

f2=open('dump.txt','rb')
d2=pickle.load(f2)
f2.close()
print(d)
