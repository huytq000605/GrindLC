class Solution {
public:
    vector<string> removeAnagrams(vector<string>& words) {
        vector<string> result;
        auto get_counter = [](string& word) {
            vector<int> counter(26);
            for(char c: word) {
                counter[c - 'a']++;
            }
            return move(counter);
        };
        for(int i = 0; i < words.size();) {
            result.push_back(words[i]);
            auto c1 = get_counter(words[i]);
            int ni = words.size();
            for(int j = i+1; j < words.size(); ++j) {
                auto c2 = get_counter(words[j]);
                bool same = true;
                for(int k = 0; k < 26; ++k) {
                    if(c1[k] != c2[k]) {
                        same = false;
                        break;
                    }
                }
                if(!same) {
                    ni = j;
                    break;
                }
            }
            i = ni;
        }
        return result;
    }
};
