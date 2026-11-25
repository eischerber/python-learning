# W1D7 = M1 正式测（闭卷 60 分钟）
# ============================================================
# 【这是什么】W1 结业验收正式卷。换一段陌生英文，限时 60 分钟，
#   独立手写 词频Top3 + 最长词 + 平均句长。过了 W1 才算真正通关。
# 【铁律】闭卷！不许打开 w1d4 / w1d5 / w1d6 抄，
#   不许 import collections / Counter、不许 sorted(..., reverse=True)、不许 lambda。
#   卡住的地方 = 还没真会的点，记下来回去补 W1D5 对应坑。
# 【为什么这样考】M1 考的是"从零把循环+字典搭出来"的肌肉记忆，看得懂≠写得出。
# ============================================================

text = "Learning to code is fun. Code helps you build apps. I write code every day and I think coding is fun. Apps can change the world. Do you like code too?"

# ── 主任务1：词频字典（手写循环）──
# 原理：lower 统一大小写 → replace 去标点 → split 切词 → 空字典累加
# TODO 1：预处理得到 words，再手写循环统计 counts（在就 +1，不在就 =1）
text = text.lower()
text_clean = text.replace(".", "").replace("?", "")
counts = {}
words = text_clean.split()
for word in words:
    if word in counts:
        counts[word]+=1
    else:
        counts[word]=1


# ── 主任务2：Top3（best 擂台法，禁 sorted/lambda）──
# 原理：for _ in range(3) 打三场；每场 best_count=-1 起手；
#   w not in top3 防连任；本场结束才 append 一次（top3 里存"词"不是元组）。
# TODO 2：基于 counts 手写三层结构得到 top3 并打印
top3 = []

for s in range(3):
    best_word = None
    best_count = -1
    for w ,c in counts.items():
        if  w not in top3  and c > best_count:
            best_word,best_count = w,c
    top3.append(best_word)
print(top3)
# ── 选做1：最长词 ──
# 原理：longest = words[0] 起手 → 逐个比 len()
# TODO 3：手写循环找出最长词并打印
longest = words[0]
for s in words:
    if len(s)>len(longest):
       longest = s 
print(longest)


# ── 选做2：平均句长 ──
# 原理：replace("?", ".").split(".") 切句 → 逐句 strip → 空串 continue
#   → 累加词数与句数 → 相除（/ 得小数）
# TODO 4：手写循环算出平均句长并打印
setences = text.replace("?",".").split(".")
total_word = 0
sentences_count = 0
for s in setences:
    s = s.strip()
    if s == "":
      continue
    total_word += len(s.split())
    sentences_count +=1
avg_setences = total_word/sentences_count
print(avg_setences)





# ============================================================
# ⚠️ 全部写完后，才允许往下看验收答案！
# ============================================================
#
# 预期输出：
#   词频 Top3：code(4) / is(2) / fun(2)
#     ⚠️ 注意：is / fun / i / you / apps 都是 2 次（并列），
#        擂台法里"先插入者先被选中"——is 比 fun 先出现，所以 is 排第 2。
#   最长词：learning（8 字母）
#   平均句长：6.2（31 词 ÷ 5 句）
#
# 三项全对 = M1 正式测过，W1 整周闭合；错哪项回去重做 W1D5 对应坑。
