####################################################################################################################################
# 05. n-gram                                                                                                                       #
# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．#
####################################################################################################################################

# coding:utf-8

def n_gram(target,n):
    result = []
    for i in range(0,len(target)-n+1):
        result.append(target[i:i+n])

    return result

target = "I am an NLPer"
words = target.split()

# 単語bi-gram
result = n_gram(words,2)
print(result)

# 文字bi-gram
result = n_gram(target,2)
print(result)