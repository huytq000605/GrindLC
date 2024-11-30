class Solution {
static constexpr int MOD = 1e9 + 7;
public:
    int sumOfGoodSubsequences(vector<int>& nums) {
        unordered_map<int, int> sum;
        unordered_map<int, int> count;
        for(int num: nums) {
            count[num] = ((count[num-1] + count[num]) % MOD + count[num+1] + 1) % MOD;
            sum[num] = ((sum[num] + sum[num-1]) % MOD + sum[num+1]) % MOD;
            sum[num] = (sum[num] + ((count[num-1] + count[num+1] + 1ll) * num) % MOD)% MOD;
        }
        int result{0};
        for(auto [k, v]: sum) {
            result = (result + v) % MOD;
        }
        return result;
    }
};
