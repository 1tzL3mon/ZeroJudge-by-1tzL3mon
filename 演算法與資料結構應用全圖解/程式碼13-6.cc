#include <iostream
#include <vector>
#include <algorithm>
using namespace std;
using Graph vector<vector<int>>;

vector<bool> seen;
vector<int> order;
void rec(const Graph &G, int v) (
    seen[v] = true;
    for (auto next_v: G[v]) {
        if (seen [next v]) continue;
        rec (6, next_v);
    }

    order.push_back(v);
}

int main() {
    int N, M;
    cin >> N >> M; // 頂點數與枝數
    Graph G(N); // 頂點數N的圖
    for (int i=0; i < M; ++i) (
        int a, b;
        cin >> a >> b;
        G[a].push_back(b);
    }
    seen.assign(N, false); //初始狀態下,全部頂點為未造訪
    order.clear(); //拓撲排序的順序
    for (int v = 0; v < N; ++v) {
        if (seen[v]) continue; //如果已造訪完畢的話不進行搜尋
        rec (G, v);
    }
    reverse (order.begin(), order.end()); //以相反順序

    for (autov: order) cout << v <<<">';
    cout << endl;
}
