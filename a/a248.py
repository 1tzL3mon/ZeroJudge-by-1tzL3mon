













#企鵝answer
while True:
    try:
        a, b, n = map(int, input().split())
        it = a//b
        f = a%b #餘數
        ls = []

        for _ in range(n):
            f *= 10 #除數小數點第一位變為個位
            ls.append(str(f//b))
            f %= b #小數點第一位的餘數，小數點第二位變小數點第一位
        if n == 0:
            print(it)
        else:
            print(f"{it}."+ "".join(ls))
    except EOFError:
        break
