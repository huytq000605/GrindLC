class Solution {
public:
    int maxSideLength(vector<vector<int>>& mat, int threshold) {
        int m = mat.size(), n = mat[0].size();
        vector<vector<int>> prefix(m+1, vector<int>(n+1, 0));
        for(int r = 0; r < m; ++r) {
            for(int c = 0; c < n; ++c) {
                prefix[r+1][c+1] = prefix[r][c+1] + prefix[r+1][c] - prefix[r][c] + mat[r][c];
            }
        }
        int result = 0;
        for(int r = 0; r < m; ++r) {
            for(int c = 0; c < n; ++c) {
                // could use binary search for s here to reduce TC from O(n) to Olog(n)
                for(int s = max(1, result); r + s <= m && c + s <= n; ++s) {
                    if(prefix[r+s][c+s] - prefix[r+s][c] - prefix[r][c+s] + prefix[r][c] <= threshold) {
                        result = max(result, s);
                    }
                }
            }
        }
        return result;
    }
};
