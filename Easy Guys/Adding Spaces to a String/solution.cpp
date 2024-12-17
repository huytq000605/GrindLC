class Solution {
public:
    string addSpaces(string s, vector<int>& spaces) {
        string result;
        for(int i{}, is{}; i < s.size(); ++i) {
            if(is < spaces.size() && i == spaces[is]) {
                result += ' ';
                ++is;
            }
            result += s[i];
        }
        return result;
    }
};
