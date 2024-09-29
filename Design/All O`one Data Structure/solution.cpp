class Node {
public:
    Node *prev, *next;
    int count;
    unordered_set<string> s;
    Node(int c) {
        count = c;
        prev = next = nullptr;
    }
};

class AllOne {
unordered_map<string, int> key_to_count;
unordered_map<int, Node*> count_to_node;
Node *head, *tail;
public:
    AllOne() {
        head = new Node(0);
        tail = new Node(0);
        head->next = tail;
        tail->prev = head;
    }
    
    void inc(string key) {
        auto count = key_to_count[key];
        auto node = count_to_node[count];
        if(!node) node = head;

        if(node->next->count != count+1) {
            auto new_node = new Node(count+1);
            auto n = node->next;
            node->next = new_node;
            new_node->prev = node;
            new_node->next = n;
            n->prev = new_node;
            count_to_node[count+1] = new_node;
        }

        ++key_to_count[key];
        node->next->s.emplace(key);

        node->s.erase(key);
        if(node != head && node->s.empty()) {
            auto p = node->prev, n = node->next;
            p->next = n;
            n->prev = p;
            count_to_node.erase(count);
            delete(node);
        }
    }
    
    void dec(string key) {
        auto count = key_to_count[key];
        auto node = count_to_node[count];

        if(count == 1) {
            key_to_count.erase(key);
        } else {
            if(node->prev->count != count-1) {
                auto new_node = new Node(count-1);
                auto p = node->prev;
                p->next = new_node;
                new_node->prev = p;
                new_node->next = node;
                node->prev = new_node;
                count_to_node[count-1] = new_node; 
            }
            
            --key_to_count[key];
            node->prev->s.emplace(key);
        }

        node->s.erase(key);
        if(node->s.empty()) {
            auto p = node->prev, n = node->next;
            p->next = n;
            n->prev = p;
            count_to_node.erase(count);
            delete(node);
        }
    }
    
    string getMaxKey() {
        if(tail->prev == head) return "";
        return *((tail->prev->s).begin());
    }
    
    string getMinKey() {
        if(head->next == tail) return "";
        return *((head->next->s).begin());
    }
};

/**
 * Your AllOne object will be instantiated and called as such:
 * AllOne* obj = new AllOne();
 * obj->inc(key);
 * obj->dec(key);
 * string param_3 = obj->getMaxKey();
 * string param_4 = obj->getMinKey();
 */
