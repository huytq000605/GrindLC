class Solution {
public:
    bool isPossibleToRearrange(string s, string t, int k) {
        unordered_map<string, int> m;
        k = s.size() / k;
        for(int i{}; i < s.size(); i += k) {
            m[s.substr(i, k)] += 1;
            m[t.substr(i, k)] -= 1;
        }
        for(auto [_, f]: m) {
            if(f) return false;
        }
        return true;
    }
};
