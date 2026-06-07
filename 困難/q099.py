import sys
from collections import defaultdict, deque
input_data = sys.stdin.read().split()
if input_data:
    n = int(input_data[0])
    words = input_data[1:1+n] #1到n
    all_chars = set() 
    for word in words:
        for char in word:
            all_chars.add(char)
    graph = defaultdict(set)
#defaultdict(set) 的神奇之處在於：當你存取一個不存在的 Key 時，它不會報錯，
#而是會自動幫你建立一個空的 set()（集合）作為該 Key 的預設值
    indegree = {char: 0 for char in all_chars} #all_chars的每個特殊char都會有一個0的字典鍵
    for i in range(n - 1): #執行n-1次
        w1 = words[i]
        w2 = words[i+1]
        min_len = min(len(w1), len(w2))
        for j in range(min_len):
            if w1[j] != w2[j]:
                if w2[j] not in graph[w1[j]]:
                    graph[w1[j]].add(w2[j])
                    indegree[w2[j]] += 1
                break
    queue = deque([char for char in all_chars if indegree[char] == 0])
    result = []
    while queue:
        curr = queue.popleft()
        result.append(curr)
        
        for nxt in graph[curr]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)
    print("".join(result))
