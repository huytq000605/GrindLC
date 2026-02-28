class Solution {
public:
    int concatenatedBinary(int n) {
        long long result = 0;
        int MOD = 1e9 + 7;
        int msb = 0;
        for(int i = 1; i <= n; ++i) {
            if((1 << msb) == i) ++msb;
            result = ((result << msb) + i) % MOD;
        }
        return result;
    }
};
