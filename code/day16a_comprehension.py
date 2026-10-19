# -*- coding: utf-8 -*-
# Day16 推导式 comprehension：把 for 循环压成一行
# 通用形式： [结果表达式 for 变量 in 可迭代对象 if 条件]
#             集合用 { }   字典用 {k: v }

# 练习1：列表推导式 —— 0~4 的平方（替代 Day15 之前的 for 循环）
squares = [x**2 for x in range(5)]
print(squares)          # [0, 1, 4, 9, 16]

# 练习2：带条件的列表推导式 —— 只留偶数
evens = [x for x in range(10) if x % 2 == 0]
print(evens)            # [0, 2, 4, 6, 8]

# 练习3：集合推导式 —— 去重（等价于 Day14 的 set(a)）
a = [1, 2, 2, 3, 3, 3]
dedup = {x for x in a}
print(dedup)            # {1, 2, 3}

# 练习4：字典推导式 —— 字符出现次数（重写 Day13 的计数循环）
text = "hello world"
counts = {ch: text.count(ch) for ch in set(text)}
print(counts)

# ---------- 你来写（练习5）----------
# 用列表推导式生成 1~10 每个数的立方（三次方 = x**3）
# 提示：range(1, 11) 是 1 到 10；立方写法 x**3
# 把下面两行取消注释，自己填 cubes 那行，再运行
# cubes = ___
# print(cubes)   # 期望输出: [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
