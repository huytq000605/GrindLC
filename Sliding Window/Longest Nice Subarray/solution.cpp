class Solution {
public:
    int longestNiceSubarray(vector<int>& nums) {
        vector<int> bits(32);
        auto valid = [&bits]() {
            for(int bit: bits) if(bit > 1) return false;
            return true;
        };
        int result = 0;
        for(int i = 0, j = 0; i < nums.size(); ++i) {
            for(int bit = 0, num = nums[i]; num > 0; num >>= 1) bits[bit++] += (num & 1);
            while(!valid()) {
                for(int bit = 0, num = nums[j]; num > 0; num >>= 1) bits[bit++] -= (num & 1);
                ++j;
            }
            result = max(result, i - j + 1);
        }
        return result;
    }
};
