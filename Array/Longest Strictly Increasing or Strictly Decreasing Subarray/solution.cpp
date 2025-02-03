class Solution {
public:
    int longestMonotonicSubarray(vector<int>& nums) {
        int result{1};
        for(int i{1}, dec{1}, inc{1}; i < nums.size(); ++i) {
            if(nums[i] > nums[i-1]) {
                inc++;
                dec = 1;
            } else if(nums[i] < nums[i-1]) {
                dec++;
                inc = 1;
            } else {
                dec = inc = 1;
            }
            result = max({result, dec, inc});
        }
        return result;
    }
};
