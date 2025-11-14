class Solution {
public:
    vector<vector<int>> rangeAddQueries(int n, vector<vector<int>>& queries) {
        vector<vector<int>> result(n, vector<int>(n));
        for(auto &q: queries) {
            int r1 = q[0], c1 = q[1], r2 = q[2], c2 = q[3];
            for(int r = r1; r <= r2; ++r) {
                result[r][c1] += 1;
                if(c2+1 < n) result[r][c2+1] -= 1;
            }
        }
       
        for(int r = 0; r < n; ++r) {
            int v = 0;
            for(int c = 0; c < n; ++c) {
                v += result[r][c];
                result[r][c] = v;
            }
        }
        return result;
    }
};
