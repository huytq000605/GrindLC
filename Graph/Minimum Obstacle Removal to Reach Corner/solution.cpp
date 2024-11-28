class Solution {
static constexpr array<pair<int, int>, 4> ds{{ {0,1}, {1,0}, {0,-1}, {-1,0} }};
public:
    int minimumObstacles(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        priority_queue<
            tuple<int, int, int>,
            vector<tuple<int, int, int>>,
            decltype([](auto t1, auto t2) -> bool {
                return get<0>(t1) > get<0>(t2);
            }) 
        > pq;
        pq.emplace(0, 0, 0);
        while(!pq.empty()) {
            auto [cost, r, c] = pq.top();
            if(r == m-1 && c == n-1) return cost;
            pq.pop();
            for(auto [dr, dc]: ds) {
                int nr = r + dr, nc = c + dc;
                if(nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
                if(grid[nr][nc] == 2) continue;
                pq.emplace(cost + grid[nr][nc], nr, nc);
                grid[nr][nc] = 2;
            }
        }

        return -1;
    }
};
