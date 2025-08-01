class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> rows(numRows, vector<int>());
        rows[0] = {1};
        for(int r = 2; r <= numRows; ++r) {
            vector<int> row(r, 1);
            for(int c = 1; c < r-1; ++c) {
                row[c] = rows[r-2][c] + rows[r-2][c-1];
            }
            rows[r-1] = std::move(row);
        }
        return rows;
    }
};
