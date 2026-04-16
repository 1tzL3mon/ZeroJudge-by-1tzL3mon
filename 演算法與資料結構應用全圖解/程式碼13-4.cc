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
