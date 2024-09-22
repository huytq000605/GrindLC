class TrieNode {
public:
    unordered_map<char, TrieNode*> map;
};

class Solution {
public:
    string longestWord(vector<string>& words) {
        sort(words.begin(), words.end(), [](auto &w1, auto &w2) -> bool {
            if(w1.size() == w2.size()) {
                return w1 > w2;
            }
            return w1.size() < w2.size();
        });
        string result;
        auto trie = new TrieNode();
        for(auto &w: words) {
            auto cur = trie;
            for(int i = 0; i < w.size(); ++i) {
                if(cur->map.find(w[i]) == cur->map.end()) {
                    if(i == w.size() - 1) {
                        cur->map[w[i]] = new TrieNode();
                        result = w;
                    }
                    break;
                }
                cur = cur->map[w[i]];
            }
            
        }
        return result;
    }
};
