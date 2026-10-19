# -*- coding: utf-8 -*-
# Day15 集合实战：交集 / 差集 / 并集
#
# 场景：两个人各自的好友名单，求
#   1. 共同好友（交集）        A & B
#   2. 只有 A 有的好友（差集）  A - B
#   3. 只有 B 有的好友（差集）  B - A
#   4. 所有人去重（并集）      A | B
#
# 核心发现：差集有【方向】——A - B 和 B - A 结果不同
#（只有A有 2 人，只有B有 1 人，输出已验证）；交集并集是对称的。

a_friends = ["张三", "李四", "王五", "赵六"]
b_friends = ["李四", "赵六", "钱七"]

# 第0步：列表 → 集合（顺便去重，集合才能做运算）
A = set(a_friends)
B = set(b_friends)
print("A:", A)
print("B:", B)

# 1. 共同好友（交集）
common = A & B
print("共同好友:", common)        # 李四、赵六

# 2. 只有 A 有的好友（差集）
only_a = A - B
print("只有A有:", only_a)         # 张三、王五

# 3. 只有 B 有的好友（差集，方向反过来）
only_b = B - A
print("只有B有:", only_b)         # 钱七

# 4. 所有人去重（并集）
everyone = A | B
print("所有人:", everyone, "共", len(everyone), "人")

# ---------- 备注 ----------
# 1. 只在一边出现的人（张三、王五、钱七）= 对称差集 A ^ B，等价于 (A-B) | (B-A)
# 2. 运算符都有等价方法写法，效果一样：
#    A & B  ==  A.intersection(B)
#    A - B  ==  A.difference(B)
#    A | B  ==  A.union(B)
#    以后看别人代码两种都会遇到，认得就行。
