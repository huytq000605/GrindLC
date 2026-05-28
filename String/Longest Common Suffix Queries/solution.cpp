struct Trie {
    Trie* chars[26];
    int iword;
    Trie(int i): iword(i) {
        for(int i = 0; i < 26; ++i) chars[i] = nullptr;
    };

    // Manually deallocate due to heap allocation
    ~Trie() {
        for(int i = 0; i < 26; ++i) {
            if(chars[i] == nullptr) continue;
            delete chars[i];
        }
    };
};

class Solution {
public:
    vector<int> stringIndices(vector<string>& wordsContainer, vector<string>& wordsQuery) {
        auto trie = new Trie(0);
        for(int iword = 0; iword < wordsContainer.size(); iword++) {
            auto &word = wordsContainer[iword];
            auto cur = trie;
            if(word.size() < wordsContainer[cur->iword].size()) 
                cur->iword = iword;
            for(int i = word.size() - 1; i >= 0; --i) {
                int j = word[i] - 'a';
                if(cur->chars[j] == nullptr) {
                    cur->chars[j] = new Trie(iword);
                }
                cur = cur->chars[j];  
                if(word.size() < wordsContainer[cur->iword].size()) 
                    cur->iword = iword;
                
            }
        }
        vector<int> result(wordsQuery.size());
        for(int ir = 0; ir < wordsQuery.size(); ++ir) {
            auto &w = wordsQuery[ir];
            auto cur = trie;
            for(int i = w.size() - 1; i >= 0; --i) {
                int j = w[i] - 'a';
                if(cur->chars[j] == nullptr) {
                    break;
                } else {
                    cur = cur->chars[j];
                }
            }
            result[ir] = cur->iword;
        }
        // Free up memory to avoid MLE
        delete trie;
        return result;
    }
};
