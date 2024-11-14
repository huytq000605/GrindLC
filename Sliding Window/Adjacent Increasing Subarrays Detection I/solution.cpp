class Solution {
public:
    bool hasIncreasingSubarrays(vector<int>& nums, int k) {
        if(k==1) return true;
        int cnt{1};
        int pa{nums[0]}, pb{nums[k]};
        for(int a{1}; a < nums.size() - k; ++a) {
            if(nums[a] <= pa || nums[a+k] <= pb) {
                cnt = 0;
            }
            ++cnt;
            if(cnt == k) return true;
            pa = nums[a];
            pb = nums[a+k];
        }
        return false;
    }
};
