import os
import csv
from konlpy.tag import Kkma
import matplotlib.pyplot as plt

f1=open(os.getcwd()+'//Today_NEWS.txt', mode='r', encoding='utf-8')
texts=f1.read()
f2=open(os.getcwd()+'//Sentimental_Dictionary.txt', mode='r',encoding='utf-8')

dic1=[]
cr=csv.reader(f2)
for row in cr:
    dic1.append(row)

def Sentiment_Analysis(text, dic):
        kkma=Kkma()
        tokens=kkma.pos(text)
        score=[]
        neg=0
        neut=0
        none=0
        pos=0
        for token in tokens:
            for item in dic:
                found=0
                found=item[0].split(";")[0].count(token[0])
                if found>0:
                    found=0
                    found=item[0].split(";")[0].count(token[1])
                    if found>0:
                        neg +=float(item[3])*float(item[8])
                        neut +=float(item[4])*float(item[8])
                        none +=float(item[5])*float(item[8])
                        pos +=float(item[6])*float(item[8])
                        break
        total=neg+neut+none+pos
        if total ==0:
            total=1
        score.append(pos/total)
        score.append(neg/total)
        score.append(neut/total)
        score.append(none/total)


        fig = plt.figure()
        fig.patch.set_facecolor('white')

        labels = 'Positive Words', 'Negative Words', 'Neutral Words', 'None-Words'
        sizes = [score[0], score[1], score[2], score[3]]
        colors = ['Blue', 'Red', 'Green', 'Grey']
        plt.axis('equal')
        plt.title('Sentimental Analysis of Naver Main News')
        plt.rcParams.update({'font.size': 12})
        _, _, autotexts = plt.pie(sizes, labels=labels, colors=colors, autopct='%1.2f%%', shadow=False, startangle=90)

        for autotext in autotexts:
            autotext.set_color('white')
        plt.show()

        return score

Sentiment_Analysis(texts, dic1)
