class Solution {
public:
    string answerString(string word, int numFriends) {
        if(numFriends == 1) return word;
        int result{};
        int target{static_cast<int>(word.size()) - numFriends + 1};
        for(int i{1}, offset{}; i < word.size(); ++i) {
            int d = word[result+offset] - word[i];
            if(d == 0) {
                ++offset;
            } else if(d < 0) {
                // dcbd
                // dcbdce
                // comparing the first character as the special case
                if(word[result] < word[i]) result = i;
                else result = i-offset;
                offset = 0;
            } else {
                offset = 0;
            }
        }
        return word.substr(result, target);
    }
};
