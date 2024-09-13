class Solution {
public:
    vector<int> resultsArray(vector<vector<int>>& queries, int k) {
        priority_queue<int, vector<int>, less<int>> pq;
        vector<int> result;
        for(auto q: queries) {
            int v = abs(q[0]) + abs(q[1]);
            pq.emplace(v);
            if(pq.size() > k) pq.pop();
            if(pq.size() < k) result.emplace_back(-1);
            else result.emplace_back(pq.top());
        }
        return result;
    }
};
