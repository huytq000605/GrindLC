class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        auto cmp = [](pair<int, int> a, pair<int, int> b) {
            return a.first < b.first;
        };
        priority_queue<pair<int, int>, 
            vector<pair<int, int>>, decltype(cmp)> pq;
        for(int c = 0; c < n; c++) {
            pq.emplace(grid[0][c], c);
            if(pq.size() > 2) {
                pq.pop();
            }
        }
        
        auto dp = grid[0];
        for(int r = 1; r < m; r++) {
            pair<int, int> mn2 = pq.top(); 
            pq.pop();
            pair<int, int> mn = pq.top();
            pq.pop();
            for(int c = 0; c < n; c++) {
                if(mn.second == c) {
                    dp[c] = mn2.first + grid[r][c];
                } else {
                    dp[c] = mn.first + grid[r][c];
                }
                pq.emplace(dp[c], c);
                if(pq.size() > 2) pq.pop();
            }
        }
        return *min_element(dp.begin(), dp.end());
    }
};
