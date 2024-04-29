class Solution {
public:
    long long subsequenceSumOr(vector<int>& nums) {
        long long bits[47] = {0};
        for(int num : nums) {
            int bit = 0;
            while(num) {
                bits[bit++] += num & 1;
                num >>= 1;
            }
        }
        long long result = 0;
        for(int bit = 0; bit < 46; bit++) {
            if(bits[bit]) result |= (static_cast<long long>(1) << bit);
            bits[bit+1] += bits[bit] / 2;
        }
        return result;
    }
};
