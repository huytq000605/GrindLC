class Solution {
public:
    bool checkValidCuts(int n, vector<vector<int>>& rectangles) {
        vector<pair<int, int>> xs, ys;
        for(auto &rec: rectangles) {
            int x1 = rec[0], x2 = rec[2];
            xs.emplace_back(x1, x2);
            int y1 = rec[1], y2 = rec[3];
            ys.emplace_back(y1, y2);
        }
        sort(xs.begin(), xs.end(), [](auto &p1, auto &p2) -> bool {
            if(p1.first == p2.first) return p1.second < p2.second;
            return p1.first < p2.first;
        });
        sort(ys.begin(), ys.end(), [](auto &p1, auto &p2) -> bool {
            if(p1.first == p2.first) return p1.second < p2.second;
            return p1.first < p2.first;
        });
        auto possible = [](vector<pair<int, int>> &intervals) -> bool {
            int mx = intervals[0].second;
            int sections{1};
            for(auto [s, e]: intervals) {
                if(s >= mx) {
                    ++sections;
                }
                mx = max(e, mx);
            }
            return sections >= 3;
        };
        
        return possible(xs) || possible(ys);
    }
};
