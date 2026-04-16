#include <iostream>
#include <vector>
using namespace std;
using Graph vector<vector<int>>;

vector<bool> seen;
void dfs(const Graph &G, int v) {
    seen [v] = true; //將v設為造訪完畢

    for (auto next_v: G[v]) {
        if (seen [next_v]) continue; //如果next_v為搜尋完畢的話不進行
        dfs(G, next_v); // 遞迴搜尋
    }
}

int main() {
    int N, M, S, t;
    cin >> N >> M >> s >> t;

    Graph G(N);
    for (int i=0; i < M; ++i) {
        int a, b;
        cin >> a >> b;
        G[a].push_back(b);
    }

    seen.assign(N, false);
    dfs(G, s);

    if (seen[t]) cout << "Yes" << endl;
    else cout << "No" << endl;
}









# 讀取點數 N, 邊數 M, 起點 s, 終點 t
n, m, s, t = map(int, input().split())

# 建立鄰接清單 (圖)
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

seen = [False] * n

def dfs(v):
    seen[v] = True
    for next_v in graph[v]:
        if not seen[next_v]:
            dfs(next_v)

# 開始搜尋並輸出結果
dfs(s)
print("Yes" if seen[t] else "No")
