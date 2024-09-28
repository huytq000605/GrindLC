class Solution {
public:
    long long minNumberOfSeconds(int mountainHeight, vector<int>& workerTimes) {
        priority_queue<
            tuple<long long, int, int>,
            vector<tuple<long long, int, int>>,
            decltype([](auto t1, auto t2) -> bool {
                return get<0>(t1) > get<0>(t2);
            })> pq;
        for(auto wt: workerTimes) {
            pq.emplace(wt, wt, 1);
        }
        long long result = 0;
        for(int i = 0; i < mountainHeight; ++i) {
            auto [t, wt, x] = pq.top();
            pq.pop();
            result = max(result, t);
            t += static_cast<long long>(wt) * (x+1);
            pq.emplace(t, wt, x+1);
        }
        return result;
    }
};
