import os
from konlpy.tag import Kkma
from more_itertools import unique_everseen

f1=open(os.getcwd()+'//POS_DOC.txt',mode='r', encoding='utf-8')
the_content1=eval(f1.read())
revised_content1=list(unique_everseen(the_content1['Positive']))
f_w1=open(os.getcwd()+'//POS_DOC.txt',mode='w', encoding='utf-8')
f_w1.write('{Positive:{')
for each in revised_content1:
    f_w1.write('"')
    f_w1.write(each)
    f_w1.write('"')
    f_w1.write(',')
    f_w1.write('\n')
f_w1.write('}}')
f_w1.close()
f1.close()

f1=open(os.getcwd()+'//POS_DOC.txt',mode='r', encoding='utf-8')
the_content1=eval(f1.read())

f2=open(os.getcwd()+'//NEG_DOC.txt',mode='r', encoding='utf-8')
the_content2=eval(f2.read())
revised_content2=list(unique_everseen(the_content2['Negative']))
f_w2=open(os.getcwd()+'//NEG_DOC.txt',mode='w', encoding='utf-8')
f_w2.write('{Negative:{')
for each in revised_content1:
    f_w2.write('"')
    f_w2.write(each)
    f_w2.write('"')
    f_w2.write(',')
    f_w2.write('\n')
f_w2.write('}}')
f_w2.close()
f2.close()

f2=open(os.getcwd()+'//POS_DOC.txt',mode='r', encoding='utf-8')
the_content2=eval(f2.read())

f3=open(os.getcwd()+'//NEU_DOC.txt',mode='r', encoding='utf-8')
the_content3=eval(f3.read())
revised_content3=list(unique_everseen(the_content3['Neutral']))
f_w3=open(os.getcwd()+'//NEU_DOC.txt',mode='w', encoding='utf-8')
f_w3.write('{Neutral:{')
for each in revised_content3:
    f_w3.write('"')
    f_w3.write(each)
    f_w3.write('"')
    f_w3.write(',')
    f_w3.write('\n')
f_w3.write('}}')
f_w3.close()
f3.close()

f3=open(os.getcwd()+'//NEU_DOC.txt',mode='r', encoding='utf-8')
the_content3=eval(f3.read())

content=[]
f=open(os.getcwd()+'//Today_NEWS.txt', mode='r',encoding='utf-8')
inside1=f.read()
inside2=inside1.replace('\n','')
inside2=inside1.replace("'","")
inside2=inside2.split(sep=' ')
kkma=Kkma()
content=kkma.nouns(inside1)

Today_News=content
Today_Positive=[]
Today_Neutral=[]
Today_Negative=[]

for i in Today_News:
    for p in the_content1['Positive']:
        if(i==p):
            Today_Positive.append(i)
    for neg in the_content2['Negative']:
        if(i==neg):
            Today_Negative.append(i)
    for neu in the_content3['Neutral']:
        if(i==neu):
            Today_Neutral.append(i)

import matplotlib.pyplot as plt
fig=plt.figure()
fig.patch.set_facecolor('white')
P=len(Today_Positive)
Neg=len(Today_Negative)
Neu=len(Today_Neutral)
labels='Positive Words', 'Negative Words', 'Neutral Words'
sizes=[P, Neg, Neu]
colors=['Blue', 'Red', 'Green']
plt.axis('equal')
plt.title('Sentimental Analysis of Naver Main News')
plt.rcParams.update({'font.size':22})
_,_,autotexts=plt.pie(sizes,labels=labels,colors=colors,
                     autopct='%1.1f%%', shadow=False, startangle=90)
for autotext in autotexts:
    autotext.set_color('white')
plt.show()