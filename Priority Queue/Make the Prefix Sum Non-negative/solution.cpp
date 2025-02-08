class Solution {
public:
    int makePrefSumNonNegative(vector<int>& nums) {
        int result{};
        priority_queue<int, vector<int>, greater<int>> pq;
        long long s{};
        for(int i{}; i < nums.size(); ++i) {
            s += nums[i];
            if(nums[i] < 0) pq.emplace(nums[i]);
            while(s < 0) {
                s -= pq.top(); pq.pop();
                ++result;
            }
        }
        return result;
    }
};
