class Solution {
public:
    bool findRotation(vector<vector<int>>& mat, vector<vector<int>>& target) {
        int n = mat.size();
        vector<bool> v(4, true);
        for(int i = 0; i < n; ++i) {
            for(int j = 0; j < n; ++j) {
                if(mat[i][j] != target[i][j]) v[0] = false;
                if(mat[i][j] != target[n-1-j][i]) v[1] = false;
                if(mat[i][j] != target[n-1-i][n-1-j]) v[2] = false;
                if(mat[i][j] != target[j][n-1-i]) v[3] = false;
            }
        }
        return v[0] || v[1] || v[2] || v[3];
        // auto rotate = [](vector<vector<int>>& mat) -> vector<vector<int>> {
        //     int n = mat.size();
        //     vector<vector<int>> result(mat);
        //     for(int i = 0; i < n; ++i) {
        //         for(int j = 0; j < n; ++j) {
        //             result[i][j] = mat[n-1-j][i];
        //         }
        //     }
        //     return result;
        // };
        // auto eq = [](vector<vector<int>>& m1, vector<vector<int>>& m2) -> bool {
        //     int n = m1.size();
        //     for(int r = 0; r < n; ++r) {
        //         for(int c = 0; c < n; ++c) if(m1[r][c] != m2[r][c]) return false;
        //     }
        //     return true;
        // };

        // if(eq(mat, target)) return true;
        // for(int i = 0; i < 3; ++i) {
        //     mat = rotate(mat);
        //     if(eq(mat, target)) return true;
        // }
        return false;
    }
};
