class Solution {
public:
    bool maxSubstringLength(string s, int k) {
        vector<int> first(26, -1);
        vector<int> last(26, -1);
        for(int i = 0; i < s.size(); ++i) {
            int c = s[i] - 'a';
            if(first[c] == -1) {
                first[c] = i;
            }
            last[c] = i;
        }
        vector<pair<int, int>> specials;
        for(int c1 = 0; c1 < 26; ++c1) {
            for(int c2 = 0; c2 < 26; ++c2) {
                if(first[c1] == -1 || first[c2] == -1) continue;
                int i = first[c1], j = last[c2];
                if(i > j || (i == 0 && j == s.size() - 1)) continue;
                bool special = true;
                for(int k = i; k <= j; ++k) {
                    auto ii = first[s[k] - 'a'], jj = last[s[k] - 'a'];
                    if(ii < i || ii > j || jj < i || jj > j) {
                        special = false;
                        break;
                    } 
                }
                if(special) specials.emplace_back(i, j);
            }
        }

        sort(specials.begin(), specials.end(), [](auto &p1, auto &p2) {
            return (p1.second - p1.first) < (p2.second - p2.first);
        });
        set<pair<int, int>> result{};
        for(auto [i, j]: specials) {
            bool valid = true;
            for(auto [ii, jj]: result) {
                if(!(i > jj || j < ii)) {
                    valid = false;
                    break;
                } 
            }
            if(valid) result.emplace(i, j);
        }
        return result.size() >= k;
    }
};
