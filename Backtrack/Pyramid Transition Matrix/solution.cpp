class Solution {
public:
    bool pyramidTransition(string bottom, vector<string>& allowed) {
        unordered_map<string, vector<char>> m;
        for (auto &s : allowed)
            m[s.substr(0, 2)].push_back(s[2]);
        auto dfs = [&](this auto&&dfs, string &bottom, string top) -> bool {
            if (top.size() == bottom.size() - 1)
                return top.empty() ? true : dfs(top, string());
            for (auto ch : m[bottom.substr(top.size(), 2)])
                if (dfs(bottom, top + ch))
                    return true;
            return false;
        };
        return dfs(bottom, string());
    }
};
