class Solution {
public:
    int maxSum(vector<int>& nums, int k) {
        vector<int> bits(32);
        for(int num: nums) {
            int bit = 0;
            while(num) {
                if(num & 1) bits[bit]++;
                num >>= 1;
                ++bit;
            }
        }

        long long result = 0;
        int MOD = 1e9 + 7;
        for(int i = 0; i < k; ++i) {
            long long num = 0;
            for(int bit = 0; bit < 32; ++bit) {
                if(bits[bit]) {
                    num += 1 << bit;
                    bits[bit]--;
                }
            }
            result = (result + (num * num % MOD)) % MOD;
        }
        return result;
    }
};
