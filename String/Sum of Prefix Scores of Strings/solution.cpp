class Trie {
public:
    Trie* m[26];
    int count;
};

class Solution {
public:
    vector<int> sumPrefixScores(vector<string>& words) {
        Trie trie;
        for(auto & w: words) {
            Trie* cur = &trie;
            for(auto & c: w) {
                if(!cur->m[c-'a']) cur->m[c-'a'] = new Trie();
                cur = cur->m[c-'a'];
                ++cur->count;
            }
        }
        vector<int> result;
        for(auto & w: words) {
            Trie* cur = &trie;
            int score = 0;
            for(auto & c: w) {
                cur = cur->m[c-'a'];
                score += cur->count;
            }
            result.emplace_back(score);
        }
        return result;
    }
};
