######################################################################################################################
# 03. 円周率                                                                                                           #
# "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，#
# 各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．                                                     #
######################################################################################################################

# coding:utf-8

target = u'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
result = []

# words = target.split(' ')
# for word in words:
#     result.append(len(word) - word.count(',') - word.count('.'))

# print(result)

words = [len(w.strip(',.')) for w in target.split()]

print(words)