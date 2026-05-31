#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m, k, d;
    if (!(cin >> n >> m >> k >> d)) return 0;

    vector<vector<int>> grid(n, vector<int>(m));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> grid[i][j];
        }
    }

    vector<vector<int>> dp(n, vector<int>(k + 1, -1));
    int INF = 2000000000;

    for (int r = 0; r < n; ++r) {
        int val = grid[r][0];
        dp[r][0] = val;
        if (k >= 1) {
            dp[r][1] = INF;
        }
    }

    for (int c = 1; c < m; ++c) {
        vector<vector<int>> next_dp(n, vector<int>(k + 1, -1));
        for (int r = 0; r < n; ++r) {
            int val = grid[r][c];
            int start_r = max(0, r - d);
            int end_r = min(n - 1, r + d);

            for (int prev_r = start_r; prev_r <= end_r; ++prev_r) {
                for (int v = 0; v <= k; ++v) {
                    if (dp[prev_r][v] == -1) continue;

                    int curr_bottleneck = min(dp[prev_r][v], val);
                    if (curr_bottleneck > next_dp[r][v]) {
                        next_dp[r][v] = curr_bottleneck;
                    }

                    if (v + 1 <= k) {
                        int curr_bottleneck_spray = dp[prev_r][v];
                        if (curr_bottleneck_spray > next_dp[r][v + 1]) {
                            next_dp[r][v + 1] = curr_bottleneck_spray;
                        }
                    }
                }
            }
        }
        dp = next_dp;
    }

    int max_ans = -1;
    for (int r = 0; r < n; ++r) {
        for (int v = 0; v <= k; ++v) {
            if (dp[r][v] > max_ans) {
                max_ans = dp[r][v];
            }
        }
    }

    cout << max_ans << "\n";

    return 0;
}

