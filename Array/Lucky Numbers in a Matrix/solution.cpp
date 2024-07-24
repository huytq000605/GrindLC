class Solution {
public:
    vector<int> luckyNumbers (vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        // Prove: we only have at most 1 lucky number in the matrix
        // let assume we have A and B are lucky numbers
        // | | | | | | |
        // _____________
        // | | |A| |C| |
        // _____________
        // | | |D| |B| |
        // That means:
        // A < C < B
        // A > D > B
        // => Contradict
        int max_min_row = 0;
        for(int r = 0; r < m; r++) {
            int mn = *min_element(matrix[r].begin(), matrix[r].end(), less<int>());
            max_min_row = max(max_min_row, mn);
        }
        int min_max_col = pow(10, 5);
        for(int c = 0; c < n; c++) {
            int mx = 0;
            for(int r = 0; r < m; r++) {
                mx = max(mx, matrix[r][c]);
            }
            min_max_col = min(min_max_col, mx);
        }
        if(min_max_col == max_min_row) return {min_max_col};
        return {};
    }
};
