class Solution {
public:
    bool divideArray(vector<int>& nums) {
        vector<int> bits(501);
        for(int num: nums) {
            bits[num] ^= 1;
        }
        return accumulate(bits.begin(), bits.end(), 0) == 0;
    }
};
