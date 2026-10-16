class Solution {
public:
    long long maxAlternatingSum(vector<int>& nums) {
        sort(begin(nums), end(nums), [](auto a, auto b) -> bool {
            return abs(a) < abs(b);
        });
        long long result = 0;
        for(int i = 0, j = nums.size() - 1; i <= j; i++, j--) {
            if(i == j) result += nums[i] * nums[i];
            else {
                result += (nums[j] * nums[j]) - (nums[i] * nums[i]);
            }
        }
        return result;
    }
};
