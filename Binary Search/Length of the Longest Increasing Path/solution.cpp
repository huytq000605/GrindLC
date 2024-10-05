class Solution {
public:
    int maxPathLength(vector<vector<int>>& coordinates, int k) {
        int x = coordinates[k][0], y = coordinates[k][1];
        sort(coordinates.begin(), coordinates.end(), [](auto& c1, auto& c2) {
            if(c1[0] == c2[0]) return c1[1] > c2[1];
            return c1[0] < c2[0];
        });
        vector<int> before, after;
        auto addLIS = [](vector<int>& l, int v) {
            auto it = lower_bound(l.begin(), l.end(), v);
            if(it == l.end()) l.emplace_back(v);
            else *it = v;
        };
        for(auto &c: coordinates) {
            if(c[0] < x && c[1] < y) {
                addLIS(before, c[1]);
            } else if(c[0] > x && c[1] > y) {
                addLIS(after, c[1]);
            }
        }
        return before.size() + 1 + after.size();
    }
};
