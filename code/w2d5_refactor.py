# -*- coding: utf-8 -*-
# W2D5（函数·重构）：把文本统计拆成多个函数，主程序 ≤ 10 行
# ============================================================
# 原理（先懂再写）：
# 1. 重构 = 功能不变，只改结构。W1D7 那 60 行流水账，逻辑你已经会了，
#    这周的任务是把它"切块装箱"——每块一个函数，各管一件事。
# 2. 为什么要拆：
#    · 主程序只写"做什么"（读起来像说明书）
#    · 函数里写"怎么做"（藏起来，不干扰主线）
#    · 哪块出 bug 只改那一个函数，不会牵一发动全身
# 3. 过关标准：主程序 ≤ 10 行（不含注释和空行）。
#    数一下下面 main 部分——现在正好 9 行，别往里塞逻辑。
# 4. 关键坑：平均句长要用【原始 text】（带句号问号），不能用 words——
#    words 已经切碎了，句子边界丢了，算不出来。
# ============================================================

TEXT = "Learning to code is fun. Code helps you build apps. I write code every day and I think coding is fun. Apps can change the world. Do you like code too?"


# ---- TODO 12：清洗文本，返回单词列表 ----
def clean_text(text):
    """统一小写、去标点、切词。

    text: 原始英文文本
    返回: 单词列表
    """

    words = text.lower().replace("?", "").replace(".", "").split()

    return words
    # 从 w1d7_m1_final.py 第 16-19 行搬：lower → replace → split


# ---- TODO 13：统计词频，返回字典 ----


def count_words(words):
    """手写循环统计每个词出现次数。

    words: 单词列表
    返回: {词: 次数} 字典
    """
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

    # 从 w1d7 第 18-24 行搬：空字典 + if/else 累加


# ---- TODO 14：Top3，返回词列表 ----
def top3(counts):
    """擂台法找出出现最多的三个词（禁 sorted/lambda）。

    counts: 词频字典
    返回: 三个词的列表
    """
    top3 = []
    for s in range(3):
        best_word = None
        best_count = -1
        for w, c in counts.items():
            if w not in top3 and c > best_count:
                best_count, best_word = c, w
    top3.append(best_word)
    return top3

    # 从 w1d7 第 31-39 行搬：for range(3) + best 起手 + 防连任


# ---- TODO 15：最长词 ----
def longest_word(words):
    """找出最长的单词。

    words: 单词列表
    返回: 最长的词（字符串）
    """
    longest = words[0]
    for s in words:
        if len(s)>len(longest):
            longest = s
    return longest        
    
    # 从 w1d7 第 44-47 行搬：longest = words[0] 起手


# ---- TODO 16：平均句长 ----
def avg_sentence_len(text):
    """计算平均每句多少个词。

    text: 原始文本（不是 words！句子边界在这里）
    返回: 平均句长（浮点数）
    """
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
    return  total_word/sentences_count

    # 从 w1d7 第 55-64 行搬：replace("?",".").split(".") → 逐句 strip → continue → += 累加
    # ⚠️ 这里必须用 += 不是 =（你昨天踩过的坑）


# ========== 主程序：9 行，不许再往里加逻辑 ==========
words = clean_text(TEXT)
counts = count_words(words)
print("Top3:", top3(counts))
print("最长词:", longest_word(words))
print("平均句长:", avg_sentence_len(TEXT))

# 预期输出：
# Top3: ['code', 'is', 'fun']
# 最长词: learning
# 平均句长: 6.2
