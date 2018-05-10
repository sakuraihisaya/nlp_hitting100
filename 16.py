#16. ファイルをN分割する
#自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．

# coding:utf-8

import math

file='hightemp.txt'
n = int(input('N--> '))

with open(file,mode='r',encoding='UTF-8') as data_file:
    lines = data_file.readlines()

count = len(lines)
unit = math.ceil(count/n)

for i,offset in enumerate(range(0,count,unit),1):
     with open('child_{:02d}.txt'.format(i),mode='w',encoding='UTF-8') as out_file:
         for line in lines[offset:offset+unit]:
             out_file.write(line)


