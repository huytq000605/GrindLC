class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        priority_queue<long long, vector<long long>, greater<long long>> pq;
        for(int num: nums) pq.emplace(num);
        int result{};
        while(pq.top() < k) {
            long long a = pq.top(); pq.pop();
            long long b = pq.top(); pq.pop();
            pq.emplace(min(a, b) * 2 + max(a, b));
            result++;
        }
        return result;
    }
};
