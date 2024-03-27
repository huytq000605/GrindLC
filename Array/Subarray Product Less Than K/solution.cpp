class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        int start = 0;
        int product = 1;
        int result = 0;
        for(int i = 0; i < nums.size(); i++) {
            product *= nums[i];
            while(start <= i && product >= k) {
                product /= nums[start];
                start += 1;
            }
            result += (i - start + 1);
        }
        return result;
    }
};
