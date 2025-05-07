class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        int mod = 0;
        for(int num: nums) mod = (mod + num%k)%k;
        return mod;
    }
};
