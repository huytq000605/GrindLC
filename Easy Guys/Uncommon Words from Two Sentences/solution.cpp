class Solution {
public:
    vector<string> uncommonFromSentences(string s1, string s2) {
        string word;
        unordered_map<string, int> words;
        for(int i = 0; i < s1.size(); ++i) {
            if(s1[i] == ' ') {
                ++words[word];
                word = "";
            } else {
                word += s1[i];
            }
            if(i == s1.size() -1) ++words[word];
        }
        word = "";
        for(int i = 0; i < s2.size(); ++i) {
            if(s2[i] == ' ') {
                ++words[word];
                word = "";
            } else {
                word += s2[i];
            }
            if(i == s2.size()-1) ++words[word]; 
        }

        vector<string> result;
        for(auto it: words) if(it.second == 1) result.emplace_back(it.first);
        return result;
    }
};
