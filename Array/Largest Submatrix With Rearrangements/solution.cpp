class Solution {
public:
    int largestSubmatrix(vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        vector<pair<int, int>> heights;
        int result = 0;
        for(int i = 0; i < n; ++i) heights.emplace_back(0, i);
        for(int r = 0; r < m; ++r) {
            vector<pair<int, int>> next_heights;
            vector<int> reset_cols;
            for(auto [h, c]: heights) {
                if(matrix[r][c]) next_heights.emplace_back(h+1, c);
                else reset_cols.push_back(c);
            }
            for(auto c: reset_cols) next_heights.emplace_back(0, c);
            heights = next_heights;
            for(int i = 0; i < n; ++i) {
                result = max(result, (i+1) * (heights[i].first));
            }
        }
        return result;
    }
};
