class Solution {
public:
    string clearStars(string s) {
        int n = s.size();
        vector<vector<int>> idxs(26);
        for(int i = 0; i < n; ++i) {
            char c = s[i];
            if(c == '*') {
                for(int i = 0; i < 26; ++i) {
                    if(!idxs[i].empty()) {
                        s[idxs[i].back()] = '*';
                        idxs[i].pop_back();
                        break;
                    }
                }
            } else {
                idxs[c-'a'].emplace_back(i);
            }
        }
        string result;
        for(int i = 0; i < n; ++i) {
            if(s[i] != '*') result += s[i];
        }
        return result;
    }
};
