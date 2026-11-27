# -*- coding: utf-8 -*-
# ============================================================
# W2D6 · sorted 的 key= 与 lambda
# 周计划原话：学生列表按成绩降序排序
#
# 【为什么学这个】
# 你 W1 做词频 Top3 时用过"手动找最大值"的循环。
# Python 内置的 sorted() 能一行完成排序，而 key= 参数让
# 你可以指定"按什么排"——这是处理成绩单、词频、文件列表
# 时最常用的技能。  
#
# 【核心语法】（先读再跑）
#   sorted(可迭代对象, key=函数, reverse=True/False)
#   - 默认升序；reverse=True 变降序
#   - key= 接一个"函数"，sorted 会用它的返回值来比大小
#   - lambda 是一次性小函数：lambda 参数: 表达式
# ============================================================

# ---------- 例 1：普通排序 ----------
nums = [5, 2, 8, 1]
print("升序:", sorted(nums))                    # [1, 2, 5, 8]
print("降序:", sorted(nums, reverse=True))      # [8, 5, 2, 1]

# ---------- 例 2：lambda 是什么 ----------
# 下面的两种写法完全等价：
def by_score(pair):        # 普通写法：一个取"第二个元素"的函数
    return pair[1]

pairs = [("葵", 74), ("小明", 92)]
print("普通函数:", sorted(pairs, key=by_score, reverse=True))
print("lambda  :", sorted(pairs, key=lambda p: p[1], reverse=True))
# lambda p: p[1] 意思是"给我一个元素 p，我返回它的 p[1]"
# sorted 就按这个返回值来比大小。

# ---------- 例 3：按字典的某个字段排 ----------
students = [
    {"name": "葵", "score": 74},
    {"name": "小明", "score": 92},
]
by_score_desc = sorted(students, key=lambda s: s["score"], reverse=True)
print("字典排序:", by_score_desc)

# ============================================================
# 【练习任务】写在下面的 TODO 区，跑通后 commit
#
# 任务 1（过关标准）：学生列表按成绩【降序】排序


#   期望输出第一行是 ("小明", 92)
#
# 任务 2：单词按长度从短到长排序（提示：key=len）

#   期望开头是 "fig"

# 任务 3（进阶）：按分数降序；同分时按名字升序
#   提示：key 返回元组 (-分数, 名字) —— 负号让分数"降序"，
#   名字保持"升序"，一次排序搞定两个条件。
#
# 过关标准：三种排序都打印出正确结果。
# 完成后：git add code/w2d6_sorted.py && git commit -m "w2d6: sorted与lambda"
# ============================================================

# ---- 在这里写你的练习代码 ----
#任务一
students = [("葵", 74), ("小明", 92), ("小红", 88), ("阿强", 92)]
level = sorted(students,key=lambda s: s[1],reverse=True)
print(level)
#任务二
words = ["banana", "apple", "cherry", "fig"]
print(sorted(words,key=len))
#任务三

    
students = [("葵", 74), ("小明", 92), ("小红", 88), ("阿强", 92)]
by_score_desc = sorted(students,key=lambda s:(-s[1],s[0]))
print(by_score_desc)