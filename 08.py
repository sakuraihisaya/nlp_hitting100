#08. 暗号文
#与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
#英小文字ならば(219 - 文字コード)の文字に置換
#その他の文字はそのまま出力
#この関数を用い，英語のメッセージを暗号化・復号化せよ．

# coding:utf-8

def cipher(target):
    result = ''
    for char in target:
        if char.islower():
            result += chr(219 - ord(char))
        else:
            result += char
    return result

target = input('文字列を入力してください：')

result1 = cipher(target)

print('暗号化結果',result1)

result2 = cipher(result1)

print('復号化結果',result2)

if result2 != target:
    print('復号化失敗！') 