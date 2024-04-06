class Solution {
public:
    long long countAlternatingSubarrays(vector<int>& nums) {
        int start = 0;
        long long result = 0;
        for(int i = 0; i < nums.size(); i++) {
            if(i > 0 && nums[i] == nums[i-1]) {
                start = i;
            }
            result += (i - start + 1);
        }
        return result;
    }
};
