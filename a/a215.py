while True: #9行
    try:
        a, b = input().split()
        n = 1
        while int(a)+int(a)*(n-1)+(n-1)*n/2 <= int(b):
            n += 1
        print(n)
    except:
        break

#企鵝answer
while True: #12行
    try:
        a,b = map(int,input().split()) #map(int,)可以把list裡的每個物件都變成int
        i = 1 
        sum = a
        while b >= sum:
            sum = sum + a + i
            i += 1
        print(i)
    except EOFError:
        break
