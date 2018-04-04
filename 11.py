# 11. タブをスペースに置換
# タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

print('ファイル名を入力してください')
file_name = input()

with open(file_name,mode='r',encoding='UTF-8') as f:
    for row in f:
        result = row.replace('\t',' ')
        print('変換前:',row,end='\n')
        print('変換後:',result,end='\n')