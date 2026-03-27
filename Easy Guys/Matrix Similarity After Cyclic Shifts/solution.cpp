class Solution {
public:
    bool areSimilar(vector<vector<int>>& mat, int k) {
        int m = mat.size(), n = mat[0].size();
        k %= n;
        if(!k) return true;
        for(int r = 0; r < m; ++r) {
            for(int c = 0; c < n; ++c) {
                if(r & 1) {
                    if(mat[r][c] != mat[r][(c-k+n)%n]) return false;
                } else {
                    if(mat[r][c] != mat[r][(c+k)%n]) return false;
                }
                
            }
        }
        return true;
    }
};
