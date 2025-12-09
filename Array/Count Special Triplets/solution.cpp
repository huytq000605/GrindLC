class Solution {
public:
    int specialTriplets(vector<int>& nums) {
        int MOD = 1e9 + 7;
        unordered_map<int, int> left, right;
        for(int num: nums) {
            right[num]++;
        }
        int result = 0;
        for(int num: nums) {
            right[num]--;
            if(left.find(num*2) != left.end() && right.find(num*2) != right.end()) {
                result = (result + (1LL * left[num*2] * right[num*2]) % MOD) % MOD;
            }
            left[num]++;
        }
        return result;
    }
};
