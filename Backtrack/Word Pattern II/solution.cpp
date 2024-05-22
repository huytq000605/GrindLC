class Solution {
public:
    bool wordPatternMatch(string pattern, string s) {
        unordered_map<char, string> mapping;
        unordered_map<string, char> reversed_mapping;
        auto dfs = [&](int i, int j) -> bool {
            auto dfs_ref = [&](int i, int j, auto dfs_ref) -> bool {
                if(i >= pattern.size() && j >= s.size()) return true;
                if(i >= pattern.size() || j >= s.size()) return false;
                if(mapping.find(pattern[i]) != mapping.end()) {
                    string st = mapping.find(pattern[i])->second;
                    if(s.substr(j, st.size()) != st) return false;
                    return dfs_ref(i+1, j + st.size(), dfs_ref);
                }
                string st;
                for(int k = j; k < s.size(); k++) {
                    st.push_back(s[k]);
                    if(reversed_mapping.find(st) != reversed_mapping.end()) continue;
                    mapping[pattern[i]] = st;
                    reversed_mapping[st] = pattern[i];
                    if(dfs_ref(i+1, k + 1, dfs_ref)) return true;
                    mapping.erase(pattern[i]);
                    reversed_mapping.erase(st);
                }

                return false;
            };

            return dfs_ref(i, j, dfs_ref);
        };

        return dfs(0, 0);
    }
};
