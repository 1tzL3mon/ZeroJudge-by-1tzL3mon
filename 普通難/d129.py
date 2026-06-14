#Ugly Number就是質因數必須為2,3或5
#1也算是Ugly Number，求出第1500個Ugly Number

ugly = [1]
p2 = p3 = p5 = 0 #乘以 2, 3, 5 的進度位置
while len(ugly) < 1500:
    next_2 = ugly[p2] * 2
    next_3 = ugly[p3] * 3
    next_5 = ugly[p5] * 5
    next_ugly = min(next_2, next_3, next_5)
    ugly.append(next_ugly)
    if next_ugly == next_2:
        p2 += 1
    if next_ugly == next_3:
        p3 += 1
    if next_ugly == next_5:
        p5 += 1
print(f"The 1500'th ugly number is {ugly[-1]}.")

# 0 0 0 = 2
# 1 0 0 = 3
# 1 1 0 = 4
# 2 1 0 = 5
# 2 1 1 = 6
# 3 2 1 = 8
#如果我們在這裡用了elif，那這一步就只會讓p2往前走，而p3還會停留在原本的位置。到了下一次循環時，next_3依然會是ugly[1]*3=6，結果清單就會被塞進第二個6

