class Solution {
public:
    int MOD = 1e9 + 7;
    long long pow_mod(long long base, long long exp) {
        if(exp == 0) return 1;
        long long result = 1;
        while(exp > 1) {
            if(exp & 1) result = (result * base) % MOD;
            base = (base * base) % MOD;
            exp >>= 1;
        }
        return (base * result) % MOD;
    }
    int countGoodNumbers(long long n) {
        long long even = (n>>1) + (n&1);
        long long odd = n >> 1;
        return (pow_mod(5, even) * pow_mod(4, odd)) % MOD;
    }
};
