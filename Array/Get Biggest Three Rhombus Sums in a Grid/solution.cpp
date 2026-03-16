class Solution {
public:
    vector<int> getBiggestThree(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        vector<vector<int>> dia1(m+1, vector<int>(n+1, 0)), dia2(m+1, vector<int>(n+2, 0));
        for(int r = 0; r < m; ++r) {
            for(int c = 0; c < n; ++c) {
                dia1[r+1][c+1] = dia1[r][c] + grid[r][c];
                dia2[r+1][c+1] = dia2[r][c+2] + grid[r][c];
            }
        }
        unordered_set<int> seen;
        priority_queue<int, vector<int>, greater<int>> pq;
        for(int r = 0; r < m; ++r) {
            for(int c = 0; c < n; ++c) {
                if(seen.find(grid[r][c]) == seen.end()) {
                    pq.push(grid[r][c]);
                    if(pq.size() > 3) pq.pop();
                    seen.insert(grid[r][c]);
                }
                
                for(int d = 1; r - d >= 0 && r + d < m && c - d >= 0 && c + d < n; ++d) {
                        int v = (dia1[r+1][c+d+1] - dia1[r-d][c]) + 
                        (dia1[r+d+1][c+1] - dia1[r][c-d]) + 
                        (dia2[r+1][c-d+1] - dia2[r-d][c+2]) + 
                        (dia2[r+d+1][c+1] - dia2[r][c+d+2]) - 
                        (grid[r+d][c] + grid[r-d][c] + grid[r][c-d] + grid[r][c+d]);
                        if(seen.find(v) == seen.end()) {
                            seen.insert(v);
                            pq.push(v);
                            if(pq.size() > 3) pq.pop();
                        }
                }
            }
        }
        vector<int> result;
        while(!pq.empty()) {
            result.push_back(pq.top());
            pq.pop();
        }
        reverse(begin(result), end(result));
        return result;
    }
};
