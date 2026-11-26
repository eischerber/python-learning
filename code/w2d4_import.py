# -*- coding: utf-8 -*-
# W2D4（函数·模块）：import 与 if __name__ == "__main__"
# ============================================================
# 原理（先懂再写）：
# 1. import：把别人写好的 .py 文件（模块）拿过来用。
#    import mymath 之后，mymath.py 里的函数就能这样调：mymath.find_range(lst)
#    ——注意要带模块名前缀，这叫"命名空间"，防止重名打架。
# 2. if __name__ == "__main__":
#    每个 .py 文件都有一个内置变量 __name__。
#    · 直接运行这个文件 → __name__ 等于 "__main__" → 代码块【执行】
#    · 被别的文件 import → __name__ 等于文件名 "mymath" → 代码块【不执行】
#    所以：自测代码放这里面。自己跑的时候测，被人 import 时不捣乱。
# 3. 这就是模块的两种身份：当"主程序"跑，或当"工具箱"被借用。
# ============================================================

# ---- 第 0 步：同目录下已有 mymath.py（我给的），先打开看一眼 ----
# 它里面有 find_range(lst) 函数 + 一个 if __name__ == "__main__" 自测块。

# ---- TODO 9：导入模块 ----
# 提示：在下面写一行 import 语句，把 mymath 引进来
import mymath

print(mymath.find_range(lst=[1,3,9,1,0,111,333,444]))



# ---- TODO 10：用模块里的函数 ----
# 用 mymath.find_range(scores) 调用，解包成 lo, hi，按格式打印
# 预期输出：最小 45 最大 96
scores = [73, 96, 45, 88, 61, 90]
lo, hi = mymath.find_range(scores)
print(lo,hi)



# ---- TODO 11：观察自测块有没有执行 ----
# 运行时如果 mymath 的自测信息【没有】打印出来 → 说明 __main__ 守卫生效了 ✅
# 如果打印了 → 说明 mymath.py 里的守卫没写对，回去检查
