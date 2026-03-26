class Solution {
public:
    bool canPartitionGrid(vector<vector<int>>& grid, bool flip = false) {
        int m = grid.size(), n = grid[0].size();
        if(m == 1) {
            vector<int> &row = grid[0];
            long long s = accumulate(begin(row), end(row), 0ll);
            long long s1 = 0;
            for(int c = 0; c < n-1; ++c) {
                s1 += row[c];
                long long s2 = s - s1;
                if(s1 - row[0] == s2 || s1 == s2 || s1 == s2 - row[c+1] || s1 == s2 - row.back()) return true;
            }
            return false;
        }
        if(!flip) {
            vector<vector<int>> ngrid(n, vector<int>(m));
            for(int r = 0; r < m; ++r) {
                for(int c = 0; c < n; ++c) {
                    ngrid[c][r] = grid[r][c];
                }
            }
            if(canPartitionGrid(ngrid, true)) return true;
        }
        if(n == 1) return false;
        unordered_map<long long, int> um1, um2;
        long long s = 0;
        for(int r = 0; r < m; ++r) {
            for(int c = 0; c < n; ++c) {
                um2[grid[r][c]]++;
                s += grid[r][c];
            }
        }
        long long s1 = 0;
        for(int r = 0; r < m-1; ++r) {
            for(int c = 0; c < n; ++c) {
                um1[grid[r][c]]++;
                s1 += grid[r][c];
                um2[grid[r][c]]--;
                if(!um2[grid[r][c]]) um2.erase(grid[r][c]);
                if(c == n-1) {
                    long long s2 = s - s1;
                    if(s1 == s2) return true;
                    long long d = abs(s1 - s2);
                    if(s1 > s2) {
                        if(r == 0 && (grid[0].front() == d || grid[0].back() == d)) return true;
                        else if(r != 0 && um1.find(d) != um1.end()) return true;
                    } else {
                        if(r == m-2 && (grid[m-1].front() == d || grid[m-1].back() == d)) return true;
                        else if(r != m-2 && um2.find(d) != um2.end()) return true;
                    }
                }
            }
        }
        return false;
    }
};
