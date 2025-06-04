class Solution {
public:
    string answerString(string word, int numFriends) {
        if(numFriends == 1) return word;
        int result{};
        int sz{static_cast<int>(word.size()) - numFriends + 1};
        for(int i{1}; i < word.size(); ++i) {
            bool lt = false;
            for(int j = 0; j < sz && i + j < word.size(); ++j) {
                if(word[result + j] > word[i + j]) break;
                if(word[result + j] < word[i + j]) {
                    lt = true;
                }
            }
            if(lt) {
                result = i;
            }
        }
        return word.substr(result, sz);
    }
};
