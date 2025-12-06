while True: #8行
    try:
        n = int(input())
    except:
        break
    if n < 0:
        n = -n
    print(n)

#企鵝answer 2行
ip = int(input())
print(abs(ip)) #abs()是絕對值功能
