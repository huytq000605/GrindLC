class Solution {
public:
    int minMoves(vector<vector<int>>& rooks) {
        int n = rooks.size();
        vector<int> rows;
        vector<int> cols;
        for(auto r: rooks) {
            rows.emplace_back(r[0]);
            cols.emplace_back(r[1]);
        }
        sort(rows.begin(), rows.end());
        sort(cols.begin(), cols.end());
        int result = 0;
        for(int i = 0; i < n; i++) {
            result += abs(rows[i] - i);
            result += abs(cols[i] - i);
        }
        return result;
    }
};
