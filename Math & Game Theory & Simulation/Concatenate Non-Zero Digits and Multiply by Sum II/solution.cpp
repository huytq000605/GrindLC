class Solution {
public:
    int MOD = 1e9 + 7;
    long long pow_mod(long long base, long long p) {
        long long result = 1;
        while(p) {
            if(p & 1) result = (result * base) % MOD;
            p >>= 1;
            base = (base * base) % MOD;
        }
        return result;
    }
    vector<int> sumAndMultiply(string s, vector<vector<int>>& queries) {
        int n = s.size();
        vector<long long> prefix_s(n);
        vector<long long> prefix_x(n);
        vector<int> lengths(n);
        for(int i = 0; i < n; ++i) {
            if(i) {
                prefix_s[i] = prefix_s[i-1];
                prefix_x[i] = prefix_x[i-1];
                lengths[i] = lengths[i-1];
            }
            if(s[i] != '0') {
                prefix_s[i] += (s[i] - '0');
                prefix_x[i] = (prefix_x[i] * 10 + s[i] - '0') % MOD;
                lengths[i] += 1;
            }
        }
        vector<int> result;
        for(auto &q: queries) {
            int i = q[0], j = q[1];
            long long s = prefix_s[j] - (i ? prefix_s[i-1]: 0);
            int d = lengths[j] - (i ? lengths[i-1]: 0);
            long long x = (prefix_x[j] - (i ? prefix_x[i-1] * pow_mod(10, d): 0)) % MOD + MOD;
            result.push_back((s*x)%MOD);
        }
        return result;
    }
};
