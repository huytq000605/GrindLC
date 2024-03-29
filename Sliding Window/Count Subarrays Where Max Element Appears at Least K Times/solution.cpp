class Solution {
public:
    long long countSubarrays(vector<int>& nums, int k) {
        int mx = *max_element(nums.begin(), nums.end());
        int count = 0, j = 0;
        long long result = 0;
        for(int i = 0; i < nums.size(); i++) {
            if(nums[i] == mx) count += 1;
            while(count >= k) {
                if(nums[j] == mx) count -= 1;
                j += 1;
            }
            result += j;
        }
        return result;
    }
};
