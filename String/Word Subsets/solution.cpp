class Solution {
public:
    vector<string> wordSubsets(vector<string>& words1, vector<string>& words2) {
        vector<int> max_freq(26);
        for(auto &w2: words2) {
            vector<int> freq(26);
            for(char c: w2) {
                freq[c-'a']++;
            }
            for(int i{}; i < 26; ++i) max_freq[i] = max(max_freq[i], freq[i]);
        }
        vector<string> result;
        for(auto &w: words1) {
            vector<int> freq(26);
            for(char c: w) {
                freq[c-'a']++;
            }
            bool valid{true};
            for(int i{}; i < 26; ++i) {
                if(max_freq[i] && max_freq[i] > freq[i]) {
                    valid = false;
                    break;
                }
            }
            if(valid) {
                result.emplace_back(w);
            }
        }
        return result;
    }
};
