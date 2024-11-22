class Solution {
public:
    int maxEqualRowsAfterFlips(vector<vector<int>>& matrix) {
        int result{};
        unordered_map<string, int> m;
        for(int r{}; r < matrix.size(); ++r) {
            string mask;
            for(int c{}; c < matrix[0].size(); ++c) {
                mask += matrix[r][c] == matrix[r][0] ? '1' : '0';
            }
            result = max(result, ++m[mask]);
        }
        return result;
    }
};
