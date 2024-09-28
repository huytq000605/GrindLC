class Solution {
public:
    bool reportSpam(vector<string>& message, vector<string>& bannedWords) {
        set<string> s(bannedWords.begin(), bannedWords.end());
        int b = 0;
        for(auto w: message) {
            if(s.find(w) != s.end()) ++b;
            if(b == 2) return true;
        }
        return false;
    }
};
