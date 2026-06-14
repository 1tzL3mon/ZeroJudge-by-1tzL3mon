#第一行代表正確答案，第二行代表接下來會有幾行
#對每次guess輸出有幾A幾B

secret = input()
n = int(input())
for _ in range(n):
    guess = input()
    a_count = 0
    b_count = 0
    for i in range(4):
        if guess[i] == secret[i]:
            a_count += 1
        elif guess[i] in secret:
            b_count += 1
    print(f"{a_count}A{b_count}B")
