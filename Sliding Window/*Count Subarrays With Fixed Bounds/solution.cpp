class Solution {
public:
    long long countSubarrays(vector<int>& nums, int minK, int maxK) {
        int imax = -1, imin = -1;
        int start = 0;
        long long result = 0;
        for(int i = 0; i < nums.size(); i++) {
            if(nums[i] < minK || nums[i] > maxK) {
                imin = imax = -1;
                start = i+1;
            }
            if(nums[i] == minK) imin = i;
            if(nums[i] == maxK) imax = i;
            if(imin != -1 && imax != -1) {
                result += (min(imin, imax) - start) + 1;
            }
        }
        return result;
    }
};
