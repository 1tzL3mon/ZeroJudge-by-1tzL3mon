# 矩陣的翻轉，行與列調換

while True:
    try:
        r, c = map(int, input().split())
        matrix = []
        for i in range(r):
            row = list(map(int, input().split()))
            matrix.append(row)
        for j in range(c): #r為1、c為2的元素會跑到r為2、c為1的位置，以此類推把矩陣翻轉
            new_row = []
            for i in range(r):
                new_row.append(str(matrix[i][j]))
            print(" ".join(new_row))
    except:
        break
