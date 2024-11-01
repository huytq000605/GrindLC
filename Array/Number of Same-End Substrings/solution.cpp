class Solution {
public:
    vector<int> sameEndSubstringCount(string s, vector<vector<int>>& queries) {
        vector<array<int, 26>> counter(s.size());
        for(int i = 0; i < s.size(); ++i) {
            if(i) counter[i] = counter[i-1];
            ++counter[i][s[i] - 'a'];
        }
        vector<int> result;
        for(auto &query: queries) {
            int a = query[0], b = query[1];
            int res = 0;
            for(int c = 0; c < 26; ++c) {
                int n = counter[b][c] - (a ? counter[a-1][c] : 0);
                res += n*(n+1)/2;
            }
            result.emplace_back(res);
        }
        return result;
    }
};
