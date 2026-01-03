start, end, step = map(int, input().split()) #split之後分別變成int
if step > 0:
    result = range(start, end + 1, step)
elif step < 0:
    result = range(start, end - 1, step)
else:
    result = [start]
print(' '.join(map(str, result))) #result裡面都先變成string之後才能join
