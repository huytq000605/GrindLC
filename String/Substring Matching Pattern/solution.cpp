class Solution {
public:
    bool hasMatch(string s, string p) {
        vector<vector<int>> memo(s.size() + 1, vector<int>(p.size() + 1, -1));
        function<bool(int, int)> match = [&](int i, int j) {
            if(j >= p.size()) return true;
            if(i >= s.size() + 1) return false;
            if(p[j] == '*') {
                memo[i][j] = match(i+1, j) || match(i, j+1);
                return static_cast<bool>(memo[i][j]);
            }
            if(i >= s.size()) return false;
            if(memo[i][j] != -1) return static_cast<bool>(memo[i][j]);            
            memo[i][j] = (s[i] == p[j] && match(i+1, j+1));
            return static_cast<bool>(memo[i][j]);
        };
        for(int i{}; i < s.size(); ++i) if(match(i, 0)) return true;
        return false;
        
    }
};
