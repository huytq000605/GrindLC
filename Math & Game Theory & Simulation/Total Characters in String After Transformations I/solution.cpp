class Solution {
static constexpr int MOD = 1000000007;
public:
    int lengthAfterTransformations(string s, int t) {
        vector<long long> counter(26);
        for(char c: s) ++counter[c - 'a'];
        for(int i = 0; i < t; ++i) {
            vector<long long> ncounter(26);
            for(int j = 0; j < 25; ++j) {
                ncounter[j+1] = counter[j];
            }
            ncounter[0] = (ncounter[0] + counter[25]) % MOD;
            ncounter[1] = (ncounter[1] + counter[25]) % MOD;
            counter = move(ncounter);
        }
        return accumulate(counter.begin(), counter.end(), 0ll) % MOD;
    }
};
