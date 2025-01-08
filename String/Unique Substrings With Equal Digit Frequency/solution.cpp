class Solution {
public:
    int equalDigitFrequency(string s) {
        int result{};
        int MOD = 1e9 + 7;
        unordered_map<int, unordered_set<int>> m;
        for(int i{}; i < s.size(); ++i) {
            int mx{}, chars{};
            vector<int> counter(26);
            long long hash{};
            for(int j{i}; j < s.size(); ++j) {
                chars += (!counter[s[j] - '0']);
                mx = max(mx, ++counter[s[j] - '0']);
                hash = (hash * 31 + (s[j] - '0')) % MOD;
                if(chars * mx == j - i + 1) {
                    auto r = m[j-i+1].emplace(hash);
                    result += r.second ? 1: 0;
                }
            }
        }
        return result;
    }
};
