class Solution {
public:
    bool validWordAbbreviation(string word, string abbr) {
        int i = 0, j = 0;
        while(i < abbr.size()) {
            if(abbr[i] == '0') return false;
            if(isdigit(abbr[i])) {
                int k = 0;
                while(i < abbr.size() && isdigit(abbr[i])) {
                    k = k*10 + (abbr[i] - '0');
                    i += 1;
                }
                j += k;
                if(j > word.size()) return false;
            } else {
                if(j >= word.size() || abbr[i] != word[j]) return false;
                i += 1;
                j += 1;
            }
        }
        return j == word.size();
    }
};
