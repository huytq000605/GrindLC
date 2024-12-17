class Solution {
public:
    vector<int> getFinalState(vector<int>& nums, int k, int multiplier) {
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        for(int i{}; i < nums.size(); ++i) {
            pq.emplace(nums[i], i);
        }
        while(k--) {
            auto [num, i] = pq.top();
            pq.pop();
            num *= multiplier;
            nums[i] = num;
            pq.emplace(num, i);
        }
        return nums;
    }
};
