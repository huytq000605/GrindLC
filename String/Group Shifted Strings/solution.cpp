class Solution {
public:
    vector<vector<string>> groupStrings(vector<string>& strings) {
        unordered_map<string, vector<string>> groups;
        for(string s: strings) {
            string group;
            for(int i = 0; i < s.size() - 1; i++) {
                group += to_string((s[i+1] - s[i] + 26) % 26) + "-";
            }
            groups[group].emplace_back(s);
        }
        vector<vector<string>> result;
        for(auto it: groups) {
            result.push_back(it.second);
        }
        return result;
    }
};
