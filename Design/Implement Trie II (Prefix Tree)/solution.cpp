class Node {
public:
    Node* chars[26];
    int word;
    int prefix;

    Node() {
        word = 0;
        prefix = 0;
        for(int i = 0; i < 26; ++i) chars[i] = nullptr;
    }
};

class Trie {
Node* root;
public:
    Trie() {
        root = new Node();
    }
    
    void insert(string word) {
        Node* cur = root;
        for(auto chr: word) {
            auto c = chr - 'a';
            if(cur->chars[c] == nullptr) {
                cur->chars[c] = new Node();
            }
            cur = cur->chars[c];
            ++(cur->prefix);
        }
        ++cur->word;
    }
    
    int countWordsEqualTo(string word) {
        Node* cur = root;
        for(auto chr: word) {
            auto c = chr - 'a';
            if(cur->chars[c] == nullptr) return 0;
            cur = cur->chars[c];
        }
        return cur->word;
    }
    
    int countWordsStartingWith(string prefix) {
        Node* cur = root;
        for(auto chr: prefix) {
            auto c = chr - 'a';
            if(cur->chars[c] == nullptr) return 0;
            cur = cur->chars[c];
        }
        return cur->prefix;
    }
    
    void erase(string word) {
        Node *cur = root;
        stack<pair<Node*, char>> s;
        for(auto chr: word) {
            auto c = chr - 'a';
            auto n = cur->chars[c];
            --n->prefix;
            if(n->prefix == 0) {
                s.emplace(cur, c);
            }
            cur = n;
        }
        --cur->word;
        while(!s.empty()) {
            auto [node, c] = s.top();
            s.pop();
            delete(node->chars[c]);
            node->chars[c] = nullptr;
        }
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * int param_2 = obj->countWordsEqualTo(word);
 * int param_3 = obj->countWordsStartingWith(prefix);
 * obj->erase(word);
 */
