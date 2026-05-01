class Solution {
public:
    int maxRotateFunction(vector<int>& nums) {
        // s1 = 0 arr[0] + 1 arr[1] + 2 arr[2] + 3 arr[3]
        // s2 = 0 arr[1] + 1 arr[2] + 2 arr[3] + 3 arr[0]
        // s2 = s1 - arr[1] - arr[2] - arr[3] + 3 arr[0]
        int s = 0;
        int sum = 0;
        int n = nums.size();
        for(int i = 0; i < n; ++i) {
            s += i * nums[i];
            sum += nums[i];
        }
        int result = s;
        for(int i = 1; i < n; ++i) {
            s = s - sum + (n) * nums[i-1];
            result = max(result, s);
        }
        return result;
    }
};
