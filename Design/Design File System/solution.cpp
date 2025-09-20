class Trie {
public:
    unordered_map<string, Trie*> t;
    int val;
    Trie() {
    }
};

class FileSystem {
Trie* trie;
public:
    FileSystem() {
        trie = new Trie();
    }
    
    bool createPath(string path, int value) {
        string cur;
        Trie* t = trie;
        for(auto c: path) {
            if(c == '/') {
                if(!cur.empty()) {
                    if(t->t.find(cur) == t->t.end()) {
                        return false;
                    }
                    t = t->t[cur];
                }
                cur = "";
            }
            else cur += c; 
        }
        if(t->t.find(cur) != t->t.end()) {
            return false;
            
        }
        t->t[cur] = new Trie();
        t = t->t[cur];
        t->val = value;
        return true;
    }
    
    int get(string path) {
        string cur;
        auto t = trie;
        for(auto c: path) {
            if(c == '/') {
                if(!cur.empty()) {
                    if(t->t.find(cur) == t->t.end()) {
                        return -1;
                    }
                    t = t->t[cur];
                }
                cur = "";
            }
            else cur += c; 
        }
        if(t->t.find(cur) == t->t.end()) {
            return -1;
        };
        t = t->t[cur];
        return t->val;
    }
};

/**
 * Your FileSystem object will be instantiated and called as such:
 * FileSystem* obj = new FileSystem();
 * bool param_1 = obj->createPath(path,value);
 * int param_2 = obj->get(path);
 */
