class Solution {
public:
    bool hasIncreasingSubarrays(vector<int>& nums, int k) {
        for(int i = 0, c = 0; i + k < nums.size(); ++i) {
            int j = i + k;
            if(i == 0 || (nums[i] > nums[i-1] && nums[j] > nums[j-1])) {
                ++c;
            } else {
                c = 1;
            }
            if(c == k) return true;
        }
        return false;
    }
};
