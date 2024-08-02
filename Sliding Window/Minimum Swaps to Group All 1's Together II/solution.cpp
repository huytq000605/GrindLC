class Solution {
public:
    int minSwaps(vector<int>& nums) {
        int n = nums.size();
        int ones = count(nums.begin(), nums.end(), 1);
        int running_ones = 0;
        int result = ones;
        for(int i = 0; i < n + ones; i++) {
            if(i >= ones) {
                running_ones -= nums[(i-ones+n)%n] == 1;
            }
            running_ones += nums[i%n] == 1;
            if(i >= ones) {
                result = min(result, ones - running_ones);
            }
        }
        return result;
    }
};
