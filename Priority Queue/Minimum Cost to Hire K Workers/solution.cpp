class Solution {
public:
    double mincostToHireWorkers(vector<int>& quality, vector<int>& wage, int k) {
        int n = quality.size();
        vector<pair<int, int>> workers(n);
        for(int i = 0; i < n; i++) {
            workers[i] = {quality[i], wage[i]};
        }
        sort(workers.begin(), workers.end(), [](auto w1, auto w2) -> bool {
            return double(w1.second) / w1.first < double(w2.second) / w2.first;
        });
        priority_queue<int, vector<int>, less<int>> pq;
        int s = 0;
        double result = double(INT_MAX);
        for(int i = 0; i < n; i++) {
            s += workers[i].first;
            pq.emplace(workers[i].first);
            if(i >= k) {
                s -= pq.top();
                pq.pop();
            }
            double rate = double(workers[i].second) / workers[i].first;
            if(i >= k-1) result = min(result, s * rate);
        }
        return result;
    }
};
