class Solution {
public:
    int snakesAndLadders(vector<vector<int>>& board) {
        int n = board.size();
        auto to_rc = [&](int sq) -> pair<int, int> {
            int r = n - 1 - sq/n;
            int c = (n-1-r) & 1 ? (n-1-(sq%n)): (sq % n);
            return {r, c};
        };
        auto to_sq = [&](int r, int c) -> int {
            int sq = (n-1-r) * n;
            sq += (n-1-r) & 1 ? (n-1-c): c;
            return sq;
        };
        auto [t1, t2] = to_rc(1);
        vector<int> ds(n*n, INT_MAX);
        ds[0] = 0;
        deque<int> dq;
        dq.emplace_back(0);
        int s = 0;
        while(!dq.empty()) {
            int m = dq.size();
            while(m--) {
                int u = dq.front(); dq.pop_front();
                if(u == n*n-1) {
                    return s;
                }
                for(int d = 1; d <= 6 && u + d < n*n; ++d) {
                    int nsq = u + d;
                    auto [nr, nc] = to_rc(nsq);
                    if(board[nr][nc] != -1) {
                        nsq = board[nr][nc] - 1;
                    }

                    if(s + 1 < ds[nsq]) {
                        ds[nsq] = s+1;
                        dq.emplace_back(nsq);
                    }
                }
            }
            ++s;
        }
        return -1;
    }
};
