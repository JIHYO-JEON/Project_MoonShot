import os

from konlpy.tag import Kkma

content=[]
f=open(os.getcwd()+'//Today_NEWS.txt', mode='r',encoding='utf-8')
inside1=f.read()
inside2=inside1.replace('\n','')
inside2=inside1.replace("'","")
inside2=inside2.split(sep=' ')
kkma=Kkma()
content=kkma.nouns(inside1)

f_w=open(os.getcwd()+'//keywords.txt', mode='w',encoding='utf-8')
for each in content:
    f_w.write('"')
    f_w.write(each)
    f_w.write('"')
    f_w.write(',')
    f_w.write('\n')
f.close()