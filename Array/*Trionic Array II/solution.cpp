class Solution {
public:
    long long maxSumTrionic(vector<int>& nums) {
        long long n = nums.size(), result = LLONG_MIN, s = nums[0];
        for(int l = 0, r = 1, p = 0, q = 0; r < n; ++r) {
            s += nums[r];
            if(nums[r] == nums[r-1]) {
                l = r;
                s = nums[r];
            } else if(nums[r] > nums[r-1]) {
                if(r > 1 && nums[r-1] < nums[r-2]) {
                    q = r-1;
                }
                if(l < p && p < q) result = max(result, s);
            } else {
                if(r > 1 && nums[r-1] > nums[r-2]) {
                    p = r-1;
                }
                while(l < q) s -= nums[l++];
                while(l+1 < p && nums[l] < 0) s -= nums[l++];
            }
        }
        return result;
    }
};
