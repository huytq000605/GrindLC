class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        int a_xor_b = 0;
        for(auto num: nums) {
            a_xor_b ^= num;
        }
        int lsb = a_xor_b & -static_cast<long long>(a_xor_b);
        int a = 0;
        for(auto num: nums) if(num & lsb) a ^= num;
        return {a, a^a_xor_b};
    }
};
