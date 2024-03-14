class Solution {
public:
    int at_most(vector<int>& nums, int k) {
        if(k < 0) return 0;
        int j = 0, s = 0, result = 0;
        for(int i = 0; i < nums.size(); i++) {
            s += nums[i];
            while(s > k) {
                s -= nums[j];
                j++;
            }
            result += (i - j + 1);
        }
        return result;
    }
    int numSubarraysWithSum(vector<int>& nums, int goal) {
        return at_most(nums, goal) - at_most(nums, goal - 1);
    }
};
