#############################################################################
# 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」                              #
#「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．#
#############################################################################

# coding:utf-8
from functools import reduce

target1 = u'パトカー'
target2 = u'タクシー'
result = ''.join(reduce(lambda x, y: x + y, zip(target1,target2)))

print(result)
