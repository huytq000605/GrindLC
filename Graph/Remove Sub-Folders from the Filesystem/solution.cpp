struct Trie {
    map<char, Trie*> m;
    int i{-1};
};

class Solution {
public:
    vector<string> removeSubfolders(vector<string>& folder) {
        vector<string> result;
        auto trie = new Trie();
        for(int i = 0; i < folder.size(); ++i) {
            auto path = folder[i];
            Trie* cur = trie;
            for(char c: path) {
                if(cur->m.find(c) == cur->m.end()) cur->m[c] = new Trie();
                cur = cur->m[c];
            }
            cur->i = i;
        }
        deque<Trie*> dq{trie};
        while(!dq.empty()) {
            auto trie = dq.front();
            dq.pop_front();
            if(trie->i != -1) result.emplace_back(folder[trie->i]);
            for(auto [c, ntrie]: trie->m) {
                if(trie->i == -1 || c != '/') dq.push_back(ntrie);
            }
        }

        return result;
    }
};
