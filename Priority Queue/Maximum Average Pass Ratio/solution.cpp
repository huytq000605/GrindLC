class Solution {
public:
    double maxAverageRatio(vector<vector<int>>& classes, int extraStudents) {
        priority_queue<pair<double, double>, vector<pair<double, double>>,
            decltype([](auto p1, auto p2) -> bool {
                auto np1 = make_pair(p1.first + 1, p1.second + 1);
                auto np2 = make_pair(p2.first + 1, p2.second + 1);
                return (np1.first / np1.second - p1.first / p1.second) < (np2.first / np2.second - p2.first / p2.second);
            })> pq;
        for(auto &cl: classes) {
            pq.emplace(cl[0], cl[1]);
        }
        while(extraStudents--) {
            auto [pass, total] = pq.top();
            pq.pop();
            pq.emplace(pass + 1, total + 1);
        }
        double s{};
        while(!pq.empty()) {
            auto [pass, total] = pq.top();
            pq.pop();
            s += pass / total;
        }
        return s / classes.size();
    }
};
