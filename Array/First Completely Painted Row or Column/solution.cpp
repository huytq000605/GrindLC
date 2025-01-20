class Solution {
public:
    int firstCompleteIndex(vector<int>& arr, vector<vector<int>>& mat) {
        int m = mat.size(), n = mat[0].size();
        vector<int> rows(m), cols(n);
        vector<pair<int, int>> rc(m*n);
        for(int r{}; r < m; ++r) {
            for(int c{}; c < n; ++c) {
                rc[mat[r][c]-1] = {r, c};
            }
        }
        for(int i{}; i < arr.size(); ++i) {
            auto [r, c] = rc[arr[i]-1];
            rows[r]++;
            if(rows[r] == n) return i;
            cols[c]++;
            if(cols[c] == m) return i;
        }

        return -1;
    }
};
