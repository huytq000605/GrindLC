class Solution {
public:
    int maxUniqueSplit(string s) {
        set<string> substrings;
        int result = 0;
        auto dfs = [&s, &substrings, &result](int i, auto dfs_ref) -> void {
            if(i >= s.size()) {
                result = max(result, static_cast<int>(substrings.size()));
                return;
            };
            string ss;
            for(int j = i; j < s.size(); ++j) {
                ss += s[j];
                if(substrings.find(ss) == substrings.end()) {
                    substrings.emplace(ss);
                    dfs_ref(j+1, dfs_ref);
                    substrings.erase(ss);
                }
            }
        };
        dfs(0, dfs);
        return result;
    }
};
