# -*- coding: utf-8 -*-
# W2D4 配套模块：mymath.py
# ============================================================
# 这是一个"工具箱"文件：只放函数，不放主流程。
# w2d4_import.py 会 import 它，借用里面的 find_range。
# ============================================================

def find_range(lst):
    """找出列表中的最小值和最大值。

    lst: 数字列表
    返回: (最小值, 最大值) 的元组
    """
    low = high = lst[0]
    for x in lst[1:]:
        if x < low:
            low = x
        if x > high:
            high = x
    return low, high


# ---- 自测块：只有直接运行 mymath.py 时才执行 ----
# 被 w2d4_import.py import 时，这里【不会】跑
if __name__ == "__main__":
    test = [7, 3, 9, 1]
    print("mymath 自测:", find_range(test))   # 预期 (1, 9)
