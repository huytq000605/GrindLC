class Solution {
public:
    vector<string> getLongestSubsequence(vector<string>& words, vector<int>& groups) {
        vector<int> looking{0, 1};
        vector<vector<string>> results(2);
        for(int i = 0; i < words.size(); ++i) {
            for(int j = 0; j < 2; ++j) {
                cout << j << " " << i << endl;
                if(looking[j] == groups[i]) {
                    looking[j] = !looking[j];
                    results[j].emplace_back(words[i]);
                }
            }
        }
        return results[0].size() >= results[1].size() ? results[0]: results[1];
    }
};
