# -*- coding: utf-8 -*-
# W1D1（2026-10-19）成绩统计：循环版 → 推导式版（两版并存对比）
#
# 背景：列表基础 / 列表方法当初是口头过的，没留代码文件，
# 所以这里一次补齐：先用循环写一遍，再用推导式改写一遍。
# 一个文件里两套写法并排，将来回看能直接看出"推导式到底省在哪"。

scores = [72, 45, 88, 91, 60, 53, 77, 96, 68, 84]

# ========== 第 1 部分：循环版（Day 12 内容，先补回来）==========
# TODO-1 平均分：用 sum() 和 len() 算，打印出来
avg = None
print("平均分:", avg)

# TODO-2 降序前三名：sorted(scores, reverse=True) 之后切片取前三个
top3 = None
print("前三名:", top3)


# ========== 第 2 部分：推导式版（Day 16 内容）==========
# 示范（这一行给你抄着找感觉）：筛出及格的成绩
passed_loop = []
for s in scores:
    if s >= 60:
        passed_loop.append(s)

passed_comp = [s for s in scores if s >= 60]   # 上面 4 行压成 1 行

print("及格（循环版）:", passed_loop)
print("及格（推导式）:", passed_comp)
print("两版结果一致:", passed_loop == passed_comp)   # 必须 True


# TODO-3 用推导式把及格分数换算成"等级"：>=85 优秀 / >=60 及格
# 提示：结果表达式里可以放三元运算  "优秀" if s >= 85 else "及格"
levels = None
print("等级:", levels)


# TODO-4 用推导式算出全班分数与平均分的差值（保留一位小数）
# 提示：round(s - avg, 1)
diffs = None
print("与平均分的差:", diffs)


# ========== 第 3 部分：自检（写完跑一遍，答案应该全对）==========
print("---- 自检 ----")
print("及格人数应为 8 →", len(passed_comp))
print("最高分应为 96 →", max(scores))
print("最低分应为 45 →", min(scores))
