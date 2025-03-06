class Solution {
public:
    vector<int> findMissingAndRepeatedValues(vector<vector<int>>& grid) {
        int n = grid.size();
        long long os = (n*n + 1) * (n*n) / 2;
        long long sq_os = 1ll*n*n*(n*n+1)*(2*n*n+1)/6;
        long long s{}, sq_s{};
        for(int i{}; i < n; ++i) {
            for(int j{}; j < n; ++j) {
                sq_s += 1ll * grid[i][j] * grid[i][j];
                s += grid[i][j];
            }
            
        }
        // a + b + B = os
        // 2 * a + B = s
        // => a - b = s - os
        // a^2 + b^2 + C = sq_os
        // 2a^2 + C = sq_s
        // => a^2-b^2 = sq_s - sq_os
        long long diff_a_b = s - os;
        long long sum_a_b = (sq_s - sq_os) / (diff_a_b);
        int a = (sum_a_b + diff_a_b)/2;
        int b = (sum_a_b - diff_a_b)/2;
        return {a,b}; 
    }
};
