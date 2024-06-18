class Solution {
public:
    int maxProfitAssignment(vector<int>& difficulty, vector<int>& profit, vector<int>& worker) {
        int n = profit.size();
        vector<pair<int, int>> jobs(n);
        for(int i = 0; i < n; i++) {
            jobs[i] = make_pair(difficulty[i], profit[i]);
        }
        sort(jobs.begin(), jobs.end(), [](auto j1, auto j2) -> bool {
            return j1.first < j2.first;
        });
        sort(worker.begin(), worker.end());
        int i = 0;
        int p = 0;
        int result = 0;
        for(auto w: worker) {
            while(i < n && jobs[i].first <= w) {
                p = max(p, jobs[i++].second);
            }
            result += p;
        }
        return result;
    }
};
