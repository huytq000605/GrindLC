class Solution {
public:
    int shortestSubarray(vector<int>& nums, int k) {
        int result = nums.size() + 1;
        vector<long long> prefix(nums.size(), 0LL);
        deque<int> dq;
        for(int i{}; i < nums.size(); ++i) {
            if(i) prefix[i] = prefix[i-1];
            prefix[i] += nums[i];
            if(prefix[i] >= k) result = min(result, i+1);
            while(!dq.empty() && prefix[i] - prefix[dq.front()] >= k) {
                result = min(result, i - dq.front());
                dq.pop_front();
            }
            while(!dq.empty() && prefix[i] <= prefix[dq.back()]) {
                dq.pop_back();
            }
            dq.emplace_back(i);
        }
        if(result == nums.size() + 1) return -1;
        return result;
    }
};
