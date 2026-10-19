# -*- coding: utf-8 -*-
# Day14 集合（set）：去重 + 交集
a = [1, 2, 2, 3, 3, 3]
print(list(set(a)))            # [1, 2, 3]  去重后转回列表

x = [1, 2, 3, 4]
y = [3, 4, 5, 6]
print(list(set(x) & set(y)))   # [3, 4]  交集
