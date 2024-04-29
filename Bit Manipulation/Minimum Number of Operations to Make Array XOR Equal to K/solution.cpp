class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        int x = 0;
        for(int num: nums) x ^= num;
        x ^= k;
        int result = 0;
        while(x) {
            result += x & 1;
            x >>= 1;
        }
        return result;
    }
};
