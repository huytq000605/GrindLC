class Solution {
public:
    int isPrefixOfWord(string sentence, string searchWord) {
        int result{1};
        bool prefix{true};
        for(int i{}, iw{}; i < sentence.size(); ++i) {
            if(sentence[i] == searchWord[iw] && prefix) ++iw;
            else {
                iw = 0;
                prefix = false;
            }
            if(iw == searchWord.size()) return result;
            if(sentence[i] == ' ') {
                ++result;
                prefix = true;
            }
        }
        return -1;
    }
};
