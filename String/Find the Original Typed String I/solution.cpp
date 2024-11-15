class Solution {
public:
    int possibleStringCount(string word) {
        int result = 1;
        int count = 1;
        for(int i = 1; i < word.size(); ++i) {
            if(word[i] == word[i-1]) {
                ++count;
            } else {
                result += (count-1);
                count = 1;
            }
        }
        result += (count-1);
        return result;
    }
};