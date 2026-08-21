while True:
    try:
        letters = list(input())
        for i in range(len(letters)-1):
            print(abs(ord(letters[i]) - ord(letters[i+1])), end='')
        print()
    except:
        break
