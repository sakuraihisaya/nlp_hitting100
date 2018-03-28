##############################################################################################################
#06. 集合                                                                                                     #
#"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，                                                   #
#それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．#
###############################################################################################################

#集合とは、重複する要素をもたない、順序づけられていない要素の集まり
#集合型の扱い：https://docs.python.jp/3/tutorial/datastructures.html#sets
#包含調査にはrepr関数かstr関数を使う：https://docs.python.jp/3/library/stdtypes.html#built-in-types

# coding:utf-8

def n_gram(target,n):
    result = []
    for i in range(0,len(target)-n+1):
        result.append(target[i:i+n])

    return result

target1 = "paraparaparadise"
target2 = "paragraph"
chech = "se"

X = set(n_gram(target1,2))
Y = set(n_gram(target2,2))

#和集合

set_or = X|Y
print('和集合：',set_or)

#積集合

set_and=X&Y
print('積集合:',set_and)

#差集合

set_sub = X-Y
print('差集合:',set_sub)

#含有調査

print("check se in X:",str('se' in X))
print("check se in X:",str('se' in Y))