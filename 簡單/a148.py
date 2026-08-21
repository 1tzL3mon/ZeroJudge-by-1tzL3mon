while True:
    try:
        scores = list(map(int, input().split()))
        average = sum(i for i in scores[1::]) / scores[0]
        print('no' if average > 59 else 'yes')
    except:
        break
