class Solution {
public:
    int findMaximizedCapital(int k, int w, vector<int>& profits, vector<int>& capital) {
        int n = profits.size();
        vector<pair<int, int>> projects(n);
        for(int i = 0; i < n; i++) {
            projects[i] = make_pair(profits[i], capital[i]);
        }
        sort(projects.begin(), projects.end(), [](auto p1, auto p2) {
            return p1.second < p2.second;
        });
        priority_queue<int, vector<int>, less<int>> pq;
        int i = 0;
        while(k--) {
            while(i < projects.size() && projects[i].second <= w) {
                pq.emplace(projects[i].first);
                i++;
            }
            if(pq.empty()) break;
            w += pq.top();
            pq.pop();
        }
        return w;
    }
};
