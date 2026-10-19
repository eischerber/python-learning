# -*- coding: utf-8 -*-
# Day14 字典实战：英文文本 → 词频字典（for 循环手写版）
#
# 演进史（4 轮踩坑，2026-10-13）：
#   1. 纯单词          → 直接数，套路照抄 Day13
#   2. 带标点          → "hello," 和 "hello" 分家 → strip() 削首尾标点
#   3. "--" 漏网       → strip 只削列出的字符 → 把 - 加进清单
#   4. 空壳词 ''       → 全标点的词削完变空串 → if word: 拦截
#
# 和 Day13 的区别：Day13 数的是【字符】（一个个字母），今天数的是【单词】。

text = "hello, -- world! hello python"

# 第1步：按空格切成单词列表
words = text.split()
print(words)

# 第2步：循环计数（strip 去标点 + 空串拦截）
counts = {}
for word in words:
    word = word.strip("-,.!?:;")
    if word:
        if word in counts:
            counts[word] = counts[word] + 1
        else:
            counts[word] = 1
print(counts)

# 方法 A 的天花板：标点永远列不全（中文标点、省略号…）。
# 治本方案 = 方法 B：只保留字母 ch.isalpha()，下次写。
