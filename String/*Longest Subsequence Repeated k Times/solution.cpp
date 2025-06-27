class Solution {
public:
    string longestSubsequenceRepeatedK(string s, int k) {
        vector<int> counter(26);
        for(char c: s) counter[c-'a']++;
        string chars;
        auto valid = [&](string &p) -> bool {
            for(int is = 0, ip = 0, matched = 0; is < s.size(); ++is) {
                if(s[is] == p[ip]) {
                    ++ip;
                    if(ip == p.size()) {
                        ++matched;
                        if(matched == k) return true;
                        ip = 0;
                    }
                }
            }
            return false;
        };
        for(int i = 25; i >= 0; --i) chars += string(counter[i] / k, i + 'a');
        string result = "";
        auto dfs = [&](this auto& dfs, string p, vector<int> &used) -> void {
            for(int i = 0; i < chars.size(); ++i) {
                if(used[i]) continue;
                string np = p + chars[i];
                if(valid(np)) {
                    if(np.size() > result.size()) result = np;
                    used[i] = 1;
                    dfs(np, used);
                    used[i] = 0;
                }
            }
        };
        vector<int> used(26);
        dfs("", used);
        return result;
    }
};
