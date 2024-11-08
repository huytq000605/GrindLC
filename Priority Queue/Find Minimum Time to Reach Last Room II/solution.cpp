class Solution {
static constexpr array<pair<int, int>, 4> ds{{ {0,1}, {1,0}, {-1,0}, {0, -1}}};
public:
    int minTimeToReach(vector<vector<int>>& A) {
        int m = A.size(), n = A[0].size();
        priority_queue<tuple<int, int, int, int>, 
            vector<tuple<int, int, int, int>>,
            decltype([](auto &t1, auto &t2) {
                return get<0>(t1) > get<0>(t2);
            })> pq;
        
        pq.emplace(0, 0, 0, 1);
        while(!pq.empty()) {
            auto [s, r, c, cost] = pq.top();
            if(r == m-1 && c == n-1) return s;
            pq.pop();
            for(auto [dr, dc]: ds) {
                int nr = r + dr, nc = c + dc;
                if(nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
                if(A[nr][nc] == -1) continue;
                pq.emplace(max(s + cost, A[nr][nc] + cost), nr, nc, 3-cost);
                A[nr][nc] = -1;
            }
        }
        return -1;
    }
};
