# 10. 行数のカウント
# 行数をカウントせよ．確認にはwcコマンドを用いよ．

# coding:utf-8

print('ファイル名を入力してください')
file_name = input()

count = 0

with open(file_name,mode='r',encoding='UTF-8') as f:
    for row in f:
        count +=  1

print(count)