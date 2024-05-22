class Solution {
public:
    vector<vector<string>> partition(string s) {
        vector<vector<string>> result;
        vector<string> partition;

        auto is_palindrome = [&](int i, int j) -> bool {
            while(i < j) {
                if(s[i++] != s[j--]) return false;
            }
            return true;
        };
        
        auto dfs = [&](int i) {
            auto dfs_ref = [&](int i, auto dfs_ref) -> void {
                if(i >= s.size()) {
                    result.emplace_back(partition);
                    return;
                }
                for(int j = i; j < s.size(); j++) {
                    if(is_palindrome(i, j)) {
                        partition.emplace_back(s.substr(i, j - i + 1));
                        dfs_ref(j+1, dfs_ref);
                        partition.pop_back();
                    }
                }
            };

            return dfs_ref(i, dfs_ref);
        };

        dfs(0);
        return result;
    }
};
