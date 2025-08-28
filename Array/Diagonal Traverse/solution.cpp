class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& mat) {
        int m = mat.size(), n = mat[0].size();
        vector<int> result;
        for(int sum_rc = 0; sum_rc < m+n-1; sum_rc++) {
            for(int x = 0; x <= sum_rc; ++x) {
                int i = x;
                int j = sum_rc - i;
                if((sum_rc & 1) == 0) swap(i, j);
                if(i >= m || j >= n) continue;
                result.push_back(mat[i][j]);
            }
        }
        return result;
    }
};
