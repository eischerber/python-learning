# W1D5 清零练习（2026-11-03）
# 目标：不看书/教程，把 W1D1–D4 踩过的 7 个坑逐个手写成【正确版本】
# 写法：每个 TODO 下方自己敲代码；写完同步在 w1d5_mistakes.md 对应栏填"我当时怎么错 + 现在怎么讲"
# 验收：7 段都能独立跑通、输出正确，不看资料

# ── 坑1：sorted 不接返回值 ──
# 原理：sorted() 返回【新列表】，原列表不动；原地排序才用 .sort()。写 sorted(a) 不接 = 白排。
# TODO：a=[3,1,2]，用 sorted 得到降序新列表 b 并打印（验证 a 没变、b 是 [3,2,1]）
a = [3, 1, 2]
b = sorted(a, reverse=True)
print(a)
print(b)


# ── 坑2：推导式/循环里丢 if ──
# 原理：条件分支漏写 if → 逻辑全错；写前先列"什么时候进分支、什么时候跳过"。
# TODO：用列表推导式从 a 里筛出 >1 的数，得到 [3, 2]

c = [3, 1, 2, 0, -1]
d = []
for x in c:
   if x > 1:
     d.append(x)
print(d)





# ── 坑3：字典键一次只能一个（取俩值用 .items() 解包）──
# 原理：d["k1","k2"] 会被当成【一个元组键】→ KeyError；想同时取键值用 for k, v in d.items()
# TODO：建 {name: score} 字典，用 .items() 找出最高分那个人并打印 "名字:分数"
students=[{"name":"小红","scores":95},
          {"name":"小明","scores":88},
          {"name":"小刚","scores":91},]
scores = {"小红": 95, "小明": 88, "小刚": 91}
best = students[0]
for s in students:
   if s["scores"]>best["scores"]:
      best = s
print(best)
   
   


# ── 坑4：top3 应为列表不是字典 ──
# 原理：要 .append() 就必须用【列表 []】，字典没有 append 方法（之前写成 {} 直接崩）。
# TODO：建空列表 top3 = []，append 三个字符串，打印 top3
q=1,2,3
top3 = []
top3.append(q)
print(top3)


# ── 坑5：Top3 只打一场擂台 ──
# 原理：要 for _ in range(3): 每轮重置 best_count=-1，且 w not in top3 防"连任"同一词。
# TODO：基于下面 counts，手写循环找 Top3（禁止 sorted / lambda），打印 ['python','is','i']
top3 = []
counts = {"python": 4, "is": 2, "fun": 1, "i": 2, "love": 1, "every": 1, "day": 1}
for i in range(3):
   best_word = None
   best_count = -1
   for w, c in counts.items():
       if w not in top3 and c > best_count:
          best_word,best_count = w, c
top3.append(best_word)

print("top3:",top3)
      



# ── 坑6：列表没 .strip() ──
# 原理：split() 后变【列表】，要进循环【逐句】 s.strip()；不能对列表整体调 .strip()（报错）。
# TODO：逐句 strip 后，跳过空串，打印每句词数
sentences = ["Python is fun", " I learn Python", "", " Do you like Python "]
for s in sentences:
   s=s.strip()
   if s =="":
      continue
   print(len(s.strip()))

# ── 坑7：去标点不接返回值 ──
# 原理：字符串【不可变】，text.replace(...) 返回新串，必须 text = text.replace(...) 重新赋值，否则白改。
# TODO：text 去标点（. 和 ?）后 split 打印干净单词列表
text = "Python is fun. I love python? Yes."

text=text.replace(".","").replace("?","")
words = text.split()


print(words)