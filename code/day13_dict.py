# -*- coding: utf-8 -*-
# Day13 字典（dict）：统计字符串中每个字符出现的次数
text = "hello world"
counts = {}
for ch in text:
    if ch in counts:
        counts[ch] = counts[ch] + 1
    else:
        counts[ch] = 1
print(counts)
