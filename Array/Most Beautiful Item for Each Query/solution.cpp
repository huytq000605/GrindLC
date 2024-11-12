class Solution {
public:
    vector<int> maximumBeauty(vector<vector<int>>& items, vector<int>& queries) {
        vector<pair<int, int>> iqueries(queries.size());
        for(int i{0}; i < queries.size(); ++i) {
            iqueries[i] = {i, queries[i]};
        }
        sort(items.begin(), items.end(), [](auto &v1, auto &v2) -> bool {
            return v1[0] < v2[0];
        });
        sort(iqueries.begin(), iqueries.end(), [](auto &a, auto &b) -> bool {
            return a.second < b.second;
        });
        vector<int> result(queries.size());
        int i{0}, mx{0};
        for(auto [q, query]: iqueries) {
            while(i < items.size() && items[i][0] <= query) {
                mx = max(mx, items[i][1]);
                ++i;
            }
            result[q] = mx;
        }
        return result;
    }
};
