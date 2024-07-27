class Solution {
public:
    long long maxScore(vector<int>& nums) {
        long long result = 0;
        int j = nums.size() - 1;
        for(int i = nums.size() - 2; i >= 0; i--) {
            if(i == 0 || nums[i] > nums[j]) {
                result += static_cast<long long>(j - i) * nums[j];
                j = i;
            }
        }
        return result;
    }
};
