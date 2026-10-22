# -*- coding: utf-8 -*-
# W1D4（2026-10-22）文本统计：词频 Top3 + 最长词 + 平均句长
#
# ⚠️ 这是 M1 的正式考试内容（10/25 考：换一段陌生英文，同样三项）。
# 今晚把这一份啃下来，D5 清零、D6 模拟测都靠它。
# 规矩：全部手写循环，不许 import collections 或用 Counter——M1 考的就是循环 + 字典。

text = "Python is fun. I learn Python every day. Coding makes me happy. Do you like Python too? I think Python is powerful."

# ---- 第 0 步：预处理（先想清楚再写）----
# 目标：把 text 变成一个干净的单词列表 words
#   1. 统一小写：text.lower()（不然 Python 和 python 会被当成两个词）
#   2. 去掉标点：至少处理 "." 和 "?"（replace 可以串着写）
#   3. 切成词：split()
# TODO：写出预处理三行，得到 words 列表


# ---- 主任务：词频字典（手写循环版）----
# 套路（Day 14 练过）：
#   counts = {} 先建空字典
#   for word in words:
#       if word in counts:  counts[word] += 1     # 见过 → 加 1
#       else:              counts[word] = 1       # 没见过 → 记 1
# TODO


# ---- 主任务：Top3（循环版，不许用 lambda 排序）----
# 套路（W1D3 刚练的 best 起手逐个比，连用三次）：
#   每次从 counts 里找「次数最多且没选过」的词
#   best_word = None; best_count = -1
#   for w, c in counts.items():
#       if w not in top3 and c > best_count:
#           best_word, best_count = w, c
#   top3.append(best_word)
# 提示：字典同时取键和值的写法是 for w, c in counts.items():
# TODO：循环三次，得到 top3 列表并打印


# ---- 选做 1：最长词 ----
# best 套路的老朋友：longest = words[0] 起手，for word in words: if len(word) > len(longest): longest = word
# TODO


# ---- 选做 2：平均句长 ----
# 思路：按句子切开 → 数每句几个词 → 累加 ÷ 句数
#   切句子：clean_text.replace("?", ".").split(".")，切完会有空字符串，要过滤掉
#   注意：split(".") 切出来每句开头多个空格，strip() 一下，空串跳过
# TODO


# ---- 自检（三项都写才有资格进 D6 模拟测）----
# 词频 Top3 应为：python(4) / i(3) / is(2)
# 最长词应为：powerful（9 个字母）
# 平均句长应为：4.4（22 个词 ÷ 5 句）
