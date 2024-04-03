class Solution {
public:
    bool isIsomorphic(string s, string t) {
        unordered_map<char, int> s_map;
        unordered_map<char, int> t_map;
        for(int i=0; i<s.size(); i++) {
            if(s_map[s[i]] == 0) s_map[s[i]] = t[i];
            if(t_map[t[i]] == 0) t_map[t[i]] = s[i];
            if(s_map[s[i]] != t[i] || t_map[t[i]] != s[i]) return false;
        }
        return true;
    }
};
