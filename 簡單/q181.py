while True:
    try:
        a, b = map(int, input().split())
        g = int(input())
        ki = list(map(int, input().split()))
        su = 0
        for i in ki:
            if i >= (i//(a+b))*(a+b)+a and i >= (2*a+b):
                su += (b-((i%(a+b))-a))
            elif i >= (i//(a+b))*(a+b) and i >= (a+b):
                su += 0
            elif i >= a:
                su += b-(i-a)
        print(su)
    except:
        break
