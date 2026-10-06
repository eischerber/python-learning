# -*- coding: utf-8 -*-
# Day15 元组 tuple：用圆括号包起来、建好就不能改的一组值
# 和 list 的区别：list 可改（可变），tuple 焊死（不可变）
# 取下标都可以：t[0] 没问题；但 t[0] = 5 会报 TypeError

# ---------- 练习1：定义元组、取下标、不可变 ----------
t = (10, 20, 30)
print(t[0])          # 10   取值可以（和 list 一样）
print(t[-1])         # 30   负下标也行：倒数第一个
print(len(t))        # 3    长度照常取

# 取消下一行注释再运行，看它报什么错（TypeError: 'tuple' object does not support item assignment）：
# t[0] = 5

# ---------- 练习2：函数一次返回多个值（元组解包）----------
# 关键：return 后面用【逗号】隔开两个值，Python 自动打包成一个元组
def min_max(nums):
    return min(nums), max(nums)      # 等价于 return (最小值, 最大值)

lo, hi = min_max([3, 1, 4, 1, 5, 9]) # 解包：把元组拆开，按顺序塞给 lo 和 hi
print(lo, hi)        # 1 9

# ---------- 验证：元组到底长啥样（你已跑通，保留）----------
r = min_max([3, 1, 4, 1, 5, 9])
print(r)             # (1, 9)   圆括号 = 元组
print(type(r))       # <class 'tuple'>

b = [1, 2, 3]
print(type(b))       # <class 'list'>
b[0] = 99            # list 可改，不报错
print(b)             # [99, 2, 3]

# ---------- 小结（当天背下来就够）----------
# 1. 逗号隔开的一组值 = 元组，括号只是看得清楚
# 2. tuple 不可变：不能改、不能加、不能删
# 3. 函数 return a, b + x, y = func() 这套组合，
#    以后调 LLM API 拿「回答 + 状态码」天天用
