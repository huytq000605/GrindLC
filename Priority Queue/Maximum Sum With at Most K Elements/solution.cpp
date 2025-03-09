class Solution {
public:
    long long maxSum(vector<vector<int>>& grid, vector<int>& limits, int k) {
        priority_queue<long long, vector<long long>, greater<long long>> pq;
        int n = grid.size(), m = grid[0].size();
        for(int r = 0; r < n; ++r) {
            priority_queue<long long, vector<long long>, greater<long long>> topk;
            for(int num: grid[r]) {
                topk.emplace(num);
                if(topk.size() > limits[r]) topk.pop();
            }
            while(!topk.empty()) {
                pq.emplace(topk.top()); topk.pop();
                if(pq.size() > k) pq.pop();
            }
        }
        long long result{};
        while(!pq.empty()) {
            result += pq.top(); pq.pop();
        }
        return result;
    }
};
