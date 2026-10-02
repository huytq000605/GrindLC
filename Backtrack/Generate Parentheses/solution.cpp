class Solution {
public:
    vector<string> generateParenthesis(int n) {
        string s;
        vector<string> result;
        auto dfs = [&](this auto& dfs, int open, int close) {
            if(close == n) {
                result.push_back(s);
                return;
            }
            if(open > close) {
                s += ")";
                dfs(open, close + 1);
                s.pop_back();
            }
            if(open < n) {
                s += "(";
                dfs(open + 1, close);
                s.pop_back();
            } 
        };
        dfs(0, 0);
        return result;
    }
};
