class Solution {
public:
    int numSpecial(vector<vector<int>>& mat) {
        int m = mat.size(), n = mat[0].size();
        int result = 0;
        vector<int> rows(m), cols(n);
        for(int r = 0; r < m; ++r) {
            for(int c = 0; c < n; ++c)
                if(mat[r][c]) {
                    rows[r]++;
                    cols[c]++;
                }
        }
        for(int r = 0; r < m; ++r) {
            for(int c = 0; c < n; ++c)
                if(mat[r][c] && rows[r] == 1 &&  cols[c] == 1) ++result;
        }
        return result;
    }
};
