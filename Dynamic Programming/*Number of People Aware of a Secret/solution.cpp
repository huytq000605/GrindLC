class Solution {
public:
    int peopleAwareOfSecret(int n, int delay, int forget) {
        vector<int> days(n+1, 0);
        days[1] = 1;
        int share = 0;
        int MOD = pow(10, 9)+7;
        for(int d = 2; d <= n; ++d) {
            share = (share + days[max(0, d-delay)]) % MOD;
            share = ((share - days[max(0, d-forget)]) % MOD + MOD) % MOD;
            days[d] = share;
        }
        int result = 0;
        for(int i = n; i >= n-forget+1; --i) result = (result + days[i]) % MOD;
        return result;
    }
};
