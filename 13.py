# 13. col1.txtとcol2.txtをマージ
# 12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．

# coding:utf-8

file1 = 'col1.txt'
file2 = 'col2.txt'

with open(file1,mode='r',encoding='UTF-8') as f1:
    with open(file2,mode='r',encoding='UTF-8') as f2:
        with open('marge.txt',mode='w',encoding='UTF-8') as m:

            for row1,row2 in zip(f1,f2):
                m.write(row1.rstrip()+'\t'+row2.rstrip()+'\n')
