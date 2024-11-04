class Solution {
public:
    string compressedString(string word) {
        string result{};
        for(int i{0}; i < word.size();) {
            char c = word[i++];
            int repeat = 1;
            while(i < word.size() && repeat < 9 && word[i] == word[i-1]) {
                ++i;
                ++repeat;
            }
            result += repeat + '0';
            result += c;
        }
        return result;
    }
};
