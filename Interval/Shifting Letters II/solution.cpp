class Solution {
public:
    string shiftingLetters(string s, vector<vector<int>>& shifts) {
        vector<int> ishift(s.size() + 1);
        for(auto &shift: shifts) {
            int s = shift[0], e = shift[1], d = shift[2];
            ishift[s] += d ? 1: -1;
            ishift[e+1] -= d ? 1: -1;
        }
        string result{};
        for(int i{}, shift{}; i < s.size(); ++i) {
            shift = ((shift + ishift[i]) % 26 + 26)% 26;
            result.push_back((s[i] - 'a' + shift) % 26 + 'a');
        }
        return result;
    }
};
