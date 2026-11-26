# -*- coding: utf-8 -*-
# ============================================================
# W2D7 · 读代码小测（W2 收官测，对应周计划的"机动：读代码小测"）
#
# 【规则】
# 1. 先别运行！每道题先在【你的预测】处写下你猜的输出
# 2. 全部预测完，再运行：python code/w2d7_codequiz.py
# 3. 对照 code/w2d7_answers.py 的答案和解释
# 4. 达标线：5 题对 4 题。不达标 → 回炉 W2D1–D3
#
# 【为什么做读代码而不是写代码】
# W2 已经练过写（D1–D5）。读代码考的是"能不能在脑子里
# 运行程序"——这是接单修 bug、读别人模板的底层能力。
# ============================================================

# ================= Q1 · 默认参数 =================
# def greet(name="同学", word="早上好"):
#     return f"{name}，{word}！"
# print(greet("葵"))
# print(greet("葵", "晚安"))
# print(greet())
# 【你的预测】（两行输出）：
#
# 【实际输出】
print("== Q1 ==")
def greet(name="同学", word="早上好"):
    return f"{name}，{word}！"
print(greet("葵"))
print(greet("葵", "晚安"))
print(greet())

# ================= Q2 · 作用域 =================
# x = 10
# def change():
#     x = 99
# change()
# print(x)
# 【你的预测】（一行输出）：
#
# 【实际输出】
print("== Q2 ==")
x = 10
def change():
    x = 99
change()
print(x)

# ================= Q3 · 多返回值 =================
# def min_max(nums):
#     return min(nums), max(nums)
# lo, hi = min_max([3, 7, 1, 9])
# print(lo, hi)
# 【你的预测】（一行输出）：
#
# 【实际输出】
print("== Q3 ==")
def min_max(nums):
    return min(nums), max(nums)
lo, hi = min_max([3, 7, 1, 9])
print(lo, hi)

# ================= Q4 · import 与 __main__ =================
# 文件 mymath.py 内容只有一行：
#     print("mymath 被加载了")
# 另一个文件运行：
#     import mymath
#     print("主程序开始")
# 【你的预测】（两行输出的顺序）：
#
# 【实际输出】（这里直接模拟 import 行为）
print("== Q4 ==")
print("mymath 被加载了")
print("主程序开始")

# ================= Q5 · sorted + lambda =================
# data = [("b", 2), ("a", 3), ("c", 1)]
# result = sorted(data, key=lambda p: p[1])
# print(result)
# 【你的预测】（一行输出）：
#
# 【实际输出】
print("== Q5 ==")
data = [("b", 2), ("a", 3), ("c", 1)]
result = sorted(data, key=lambda p: p[1])
print(result)

# ============================================================
# 跑完后打开 code/w2d7_answers.py 对答案。
# 把每题对错记到 Obsidian；≥4 对 → W2 完成，进 W3 项目；
# ≤3 对 → 回炉 w2d1_function.py 到 w2d3_docstring.py。
# ============================================================
