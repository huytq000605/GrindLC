class Solution {
public:
    long long countSubarrays(vector<int>& nums, long long k) {
        long long s = 0;
        long long result = 0;
        for(long long i = 0, j = 0; i < nums.size(); ++i) {
            s += nums[i];
            while(s * (i - j + 1) >= k) {
                s -= nums[j];
                ++j;
            }
            result += (i-j+1);
        }
        return result;
    }
};
