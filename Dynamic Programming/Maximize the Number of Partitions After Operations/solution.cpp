class Solution {
public:
    int maxPartitionsAfterOperations(string s, int k) {
        unordered_map<long long, int> cache;
        auto dfs = [&](this auto&& dfs, long long i, long long mask, int can_change) -> int {
            long long key = (i << 27) | (mask << 1) | can_change;
            if(cache.find(key) != cache.end()) return cache[key];
            if(i >= s.size()) return 1;
            int nmask = mask | (1 << (s[i] - 'a'));
            int set_bits = __popcount(nmask);
            int result = 0;
            if(set_bits <= k) result = dfs(i+1, nmask, can_change);
            else result = 1 + dfs(i+1, 1 << (s[i] - 'a'), can_change);
            if(can_change) {
                for(int c = 0; c < 26; ++c) {
                    if(c == s[i] - 'a' || (mask >> c) & 1) continue;
                    int nmask = mask | (1 << c);
                    int set_bits = __popcount(nmask);
                    if(set_bits <= k) result = max(result, dfs(i+1, nmask, 0));
                    else result = max(result, 1 + dfs(i+1, 1 << c, 0));
                }
            }
            return cache[key] = result;
        };
        return dfs(0ll, 0ll, 1);
    }
};
