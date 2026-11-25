# W2D3（函数·下）：多返回值 + 文档字符串 docstring
# ============================================================
# 原理（先懂再写）：
# 1. 多返回值：return a, b 其实返回的是一个【元组 (a, b)】，
#   调用处用解包接住：lo, hi = find_range(lst)
#    ——这就是 W1 你学过的"元组与解包"在函数里的正式登场。
# 2. docstring：函数体第一行写三引号字符串 """..."""，
#    它就是函数的"说明书"。好处：别人（包括未来一个月的你）
#    只读说明书就知道怎么用，不用读实现。
#    约定格式：第一句干什么 → 参数什么意思 → 返回什么。
# 3. 有了 docstring，VS Code 鼠标悬停在函数名上会自动显示——
#    这就是 W2D3 过关标准"只读文档的人会用"的原理。
# ============================================================

# ---- 主任务：写 find_range(lst)，同时返回最小值和最大值 ----
# TODO 6：def find_range(lst): 一次遍历同时找 min 和 max（best 起手逻辑用两份），
#          return 两个值；函数第一行写完整 docstring
# 要求：docstring 至少包含——功能一句话 / 参数 lst 是什么 / 返回值是什么
def find_range(lst):
    """找出列表中的最小值和最大值。
        
        lst:数字列表
        返回：(最小值，最大值)的元组
         """
    low =high = lst[0]
    for x in lst[1:]:
        if x < low:
            low = x
        if x > high:
           high = x
    return low,high 



    
scores = [73, 96, 45, 88, 61, 90]

# ---- 验收：解包接住两个返回值 ----
# 预期输出：
# 最小 45 最大 96
# TODO 7：调用 + 解包 + 按预期格式打印
lo,hi = find_range(scores)
print(lo,hi)



# ---- 附加：验证"return 多值 = 元组" ----
# 预测：print(find_range(scores)) 的输出类型和内容是什么？
# TODO 8：直接 print 整个返回值，看它是不是元组，验证预测
print(find_range(scores))
scores = [73, 96, 45, 88, 61, 90]
