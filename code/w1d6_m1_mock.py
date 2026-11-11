# W1D6 = M1 模拟测（补做日 2026-11-11）
# ============================================================
# 【这是什么】W1 结业验收的模拟卷。M1 正式测要求：换一段陌生英文，
#   限时 60 分钟，独立完成 词频Top3 + 最长词 + 平均句长。
# 【铁律】闭卷！不许打开 w1d4_textstat.py / w1d5_practice.py 抄，
#   不许 import collections / Counter、不许 sorted(..., reverse=True)、不许 lambda。
#   卡住的地方 = 你还没真会的点，记下来回去补，别翻旧代码。
# 【为什么这样考】M1 考的是"从零把循环+字典搭出来"的肌肉记忆，
#   不是"能不能跑通"。所以必须脱稿手写，看得懂≠写得出。
# ============================================================

text = "Python is great. I use Python every day. Python helps me solve tasks and I think Python is powerful. Data science uses Python too. Many people learn Python because it is simple."

# ── 主任务1：词频字典（手写循环）──
# 原理：空字典 counts = {} → for word in words → 在就 +1，不在就 =1。
# TODO：预处理（lower → 去 . 和 ? → split）得到 words，再手写循环统计词频。
clean_text = text.replace("?","").replace(".","")
counts = {}
words = clean_text.lower().split()

for word in words:
    if word in counts:
       counts[word] +=1
    else:
        counts[word] = 1

    


# ── 主任务2：Top3（best 擂台法，禁 sorted/lambda）──
# 原理：for _ in range(3) 打三场；每场 best_count=-1 起手；
#   w not in top3 防同一个词连任；本场结束才 append 一次。
# TODO：基于上面的 counts，手写三层结构得到 top3 并打印。
top3 = []

for  i in range(3):
    best_count=-1
    best_word=None
    for w ,c in counts.items():
        if w not in top3 and c > best_count:
            best_word, best_count = w,c
            
    top3.append(best_word)
print(top3)
# ── 选做1：最长词 ──
# 原理：longest = words[0] 起手 → 逐个比 len()，大就换人。
# TODO：手写循环找出最长词并打印。
longest = words[0]
for s in words:
    if len(s)>len(longest):
        longest = s
print(longest)
# ── 选做2：平均句长 ──
# 原理：replace("?", ".").split(".") 切句 → 逐句 strip → 空串 continue
#   → 累加词数与句数 → 相除（/ 得小数）。
# TODO：手写循环算出平均句长并打印。
setences=text.replace("?",".").split(".")
total_word = 0
setences_count=0
for s in setences:
    s = s.strip()
    if s =="":
        continue
    total_word += len(s.split())
    setences_count += 1
avg_setences = total_word/setences_count
print(avg_setences)






# ============================================================
# ⚠️ 以上全部写完后，才允许往下看验收答案！
# ============================================================
#
# 预期输出：
#   词频 Top3：python(6) / is(3) / i(2)
#   最长词：powerful（8 字母）
#   平均句长：6.4（32 词 ÷ 5 句）
#
# 三项全对 = M1 过；错哪项就回去重做 W1D5 对应的坑（错题本里有口诀）。
