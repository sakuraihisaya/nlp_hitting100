# 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
# 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．

# coding:utf-8

file_name = 'hightemp.txt'

with open(file_name,mode = 'r',encoding='UTF-8') as f,open('col1.txt',mode = 'w') as col1,open('col2.txt',mode = 'w') as col2:
    for row in f:
        cols = row.split('\t')
        col1.write(cols[0] + '\n')
        col2.write(cols[1] + '\n')