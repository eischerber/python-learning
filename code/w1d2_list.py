# -*- coding: utf-8 -*-
# W1D2（2026-10-20）列表四合一 · 脱稿重写
#
# 昨天（W1D1）写过同样四样，今天是合上昨天的代码再写一遍。
# 规则：不许打开 w1d1_grades.py 抄；忘了语法可以查自己的错题笔记。
# 每段注释写清这段在算什么——W1D5 清零日要回看这个文件。

scores = [90, 55, 78, 88, 62, 95, 71, 83, 59, 100, 66]

# ---- 1. 最大值 ----
# 思路：内置 max()，或者 for 循环逐个比大小（初始化 m = scores[0]）
# TODO：求出最大值，打印出来
max_scores = max(scores)
print(max_scores)

# ---- 2. 最小值 ----
# TODO
min_scores = min(scores)
print(min_scores)


# ---- 3. 平均分 ----
# 思路：sum(scores) / len(scores)
# TODO
avg = (sum(scores)/len(scores))
print(avg)


# ---- 4. 降序前三名 ----
# 思路：先 sorted(scores, reverse=True) 得到新列表，再切片 [:3]
# 注意：sorted() 不改原列表，必须把返回值接住
# TODO
desc = sorted(scores,reverse=True)
top3 = desc[:3]
print(top3)


# ---- 自检（写完跑一遍，四行全对才算过）----
# 最大值应为 100
# 最小值应为 55
# 平均分应为 77.0
# 前三名应为 [100, 95, 90]


# ================= 参考答案（先自己写，写完再对照）=================
# max_score = max(scores)
# min_score = min(scores)
# avg = sum(scores) / len(scores)
# top3 = sorted(scores, reverse=True)[:3]
# 用循环的写法：m = scores[0]; for s in scores: if s > m: m = s
# =================================================================
