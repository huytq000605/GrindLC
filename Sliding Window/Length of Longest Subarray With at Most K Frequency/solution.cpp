class Solution {
public:
    int maxSubarrayLength(vector<int>& nums, int k) {
        std::unordered_map<int, int> counter;
        int result = 0, start = 0;
        for(int i = 0; i < nums.size(); i++) {
            counter[nums[i]]++;
            while(counter[nums[i]] > k) {
                counter[nums[start++]] -= 1;
            }
            result = std::max(result, i - start + 1);
        }
        return result;
    }
};
