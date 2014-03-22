# coding: utf-8

from nltk.book import *

# 試行錯誤と書いてあったが、
# 英文の場合. が必ずつくと仮定して
# 前後の. を発見することで解いた
sunset_index = text9.index('sunset')

for (n, w) in enumerate(text9[sunset_index:]):
     if w == '.':
         period_index = n + sunset_index
         break

for (n, w) in enumerate(reversed(text9[:text9.index('sunset')])):
     if w == '.':
         before_period_index = sunset_index - n
         break

print ' '.join(text9[before_period_index:period_index+1])
