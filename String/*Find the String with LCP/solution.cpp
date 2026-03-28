class Solution {
public:
    string findTheString(vector<vector<int>>& lcp) {
        int n = lcp.size();
        string result(n, ' ');
        char c = 'a';
        for(int i = 0; i < n; ++i) {
            if(result[i] != ' ') continue;
            if(c > 'z') return "";
            result[i] = c;
            for(int j = 0; j < n; ++j) {
                if(lcp[i][j]) {
                    if(j < i && result[j] != result[i]) return "";
                    result[j] = c;
                }
            }
            ++c;
        }
        vector<vector<int>> res_lcp(n, vector<int>(n, 0));
        for(int i = n-1; i >= 0; --i) {
            for(int j = n-1; j >= 0; --j) {
                res_lcp[i][j] = result[i] == result[j] ? (i+1 < n && j+1 < n ? res_lcp[i+1][j+1] + 1: 1): 0;
                if(res_lcp[i][j] != lcp[i][j]) return "";
            }
            
        }
        return result;
    }
};
