class Solution {
public:
    int largestInteger(vector<int>& nums, int k) {
        if(nums.size() == k) {
            return *max_element(nums.begin(), nums.end());
        }
        vector<int> counter(51);
        for(int num: nums) {
            counter[num]++;
        }
        int result = -1;
        if(k == 1) {
            for(int num = 0; num <= 50; ++num) {
                if(!counter[num] || counter[num] > 1) continue;
                result = max(result, num);
            }
        } else {
            if(counter[nums[0]] == 1) result = max(result, nums[0]);
            if(counter[nums.back()] == 1) result = max(result, nums.back());
        }
        return result;
    }
};
