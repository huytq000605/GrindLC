struct Node {
    Node *prev, *next;
    int k, v;

    Node(int _k = -1, int _v = 0, Node* _prev = nullptr, Node* _next = nullptr): k(_k), v(_v), prev(_prev), next(_next) {};
};

class LRUCache {
int cap;
Node *head, *tail;
unordered_map<int, Node*> key_to_node;

public:
    LRUCache(int capacity) {
        cap = capacity;
        head = new Node(-1, -1);
        tail = new Node(-1, -1, head);
        head->next = tail;
    }

    void remove(Node* node) {
        auto prev = node->prev;
        auto next = node->next;
        prev->next = next;
        next->prev = prev;
    }

    void move_to_tail(Node* node) {
        node->prev = tail->prev;
        node->next = tail;
        tail->prev->next = node;
        tail->prev = node;
    }
    
    int get(int key) {
        if(key_to_node.find(key) == key_to_node.end()) return -1;
        auto node = key_to_node[key];
        remove(node);
        move_to_tail(node);
        
        return key_to_node[key]->v;
    }
    
    void put(int key, int value) {
        if(key_to_node.find(key) == key_to_node.end()) {
            if(key_to_node.size() == cap) {
                auto node = head->next;
                key_to_node.erase(node->k);
                remove(node);
            }
            auto node = new Node(key, value);
            key_to_node[key] = node;
            move_to_tail(node);
        } else {
            auto node = key_to_node[key];
            node->v = value;
            remove(node);
            move_to_tail(node);
        }
        return;
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
