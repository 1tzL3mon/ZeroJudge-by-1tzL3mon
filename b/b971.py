start, end, step = map(int, input().split()) #split之後分別變成int
if step > 0:
    result = range(start, end + 1, step) #最多可以到end的公差為step的正向等差數列（step必須為正的）
elif step < 0:
    result = range(start, end - 1, step) #最多可以到end的公差為step的負向等差數列（step必須為負的）
else:
    result = [start]
print(' '.join(map(str, result))) #result裡面都先變成string之後才能join
