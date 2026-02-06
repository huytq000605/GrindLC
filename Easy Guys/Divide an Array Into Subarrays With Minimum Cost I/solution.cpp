class Solution {
public:
    int minimumCost(vector<int>& nums) {
        priority_queue<int> pq;
        for(int i = 1; i < nums.size(); ++i) {
            pq.emplace(nums[i]);
            if(pq.size() > 2) pq.pop();
        }
        int result = nums[0];
        while(!pq.empty()) {
            result += pq.top(); pq.pop();
        }
        return result;
    }
};
