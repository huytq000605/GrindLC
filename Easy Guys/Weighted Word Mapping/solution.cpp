class Solution {
public:
    string mapWordWeights(vector<string>& words, vector<int>& weights) {
        string result;
        for(auto &word: words) {
            int w = 0;
            for(char c: word) {
                w += weights[c - 'a'];
            }
            result += (25 - (w % 26) + 'a');
        }
        return result;
    }
};
