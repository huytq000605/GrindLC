class Solution {
public:
    int maxScoreWords(vector<string>& words, vector<char>& letters, vector<int>& score) {
        unordered_map<int, int> letter_counter;
        for(auto letter: letters) {
            letter_counter[letter - 'a'] += 1;
        }
        auto dfs = [&](int i, auto dfs) -> int {
            if(i >= words.size()) return 0;
            auto ret = dfs(i + 1, dfs);
            bool valid = true;
            unordered_map<int, int> counter;
            for(auto c: words[i]) {
                counter[c - 'a'] += 1;
                if(counter[c-'a'] > letter_counter[c - 'a']) {
                    valid = false;
                    break;
                }
            }
            if(valid) {
                int s = 0;
                for(auto it: counter) {
                    letter_counter[it.first] -= it.second;
                    s += it.second * score[it.first];
                }
                ret = max(ret, dfs(i+1, dfs) + s);
                for(auto it: counter) {
                    letter_counter[it.first] += it.second;
                }
            }
            return ret;
        };

        return dfs(0, dfs);
    }
};
