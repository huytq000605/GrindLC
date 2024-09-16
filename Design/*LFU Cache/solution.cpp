class Node {
public:
    int key, value;
    Node *prev, *next;
    Node(int k, int v) {
        key = k;
        value = v;
    }
};

class DLL {
public:
    Node *head, *tail;
    int s;
    DLL() {
        head = new Node(0, 0);
        tail = new Node(0, 0);
        head->next = tail;
        tail->prev = head;
        s = 0;
    }
    void erase(Node* node) {
        Node *p = node->prev, *n = node->next;
        p->next = n;
        n->prev = p;
        --s;
    }
    void emplace(Node* node) {
        Node *p = tail->prev;
        p->next = node;
        tail->prev = node;
        node->next = tail;
        node->prev = p;
        ++s;
    }
    Node* pop_front() {
        Node *node = head->next, *n = node->next;
        head->next = n;
        n->prev = head;
        --s;
        return node;
    }
    int size() {
        return s;
    }
};

class LFUCache {
private:
    int cap, min_count, size;
    map<int, Node*> key_to_node;
    map<int, int> key_to_count;
    map<int, DLL*> count_to_dll;
public:
    LFUCache(int capacity) {
        cap = capacity;
        size = 0;
        min_count = 0;
    }
    
    int get(int key) {
        if(key_to_node.find(key) == key_to_node.end()) return -1;
        Node* node = key_to_node[key];
        int count = key_to_count[key];
        DLL* dll = count_to_dll[count];
        dll->erase(node);
        if(dll->size() == 0 && min_count == count) ++min_count;

        ++count;
        if(count_to_dll.find(count) == count_to_dll.end()) count_to_dll[count] = new DLL();
        dll = count_to_dll[count];
        dll->emplace(node);
        key_to_count[key] = count;
        return node->value;
    }
    
    void put(int key, int value) {
        if(key_to_node.find(key) == key_to_node.end()) {
            Node* node = new Node(key, value);
            if(size == cap) {
                Node* node = count_to_dll[min_count]->pop_front();
                key_to_node.erase(node->key);
                key_to_count.erase(node->key);
                delete(node);
                --size;
            }
            key_to_node[key] = node;
            key_to_count[key] = 1;
            if(count_to_dll.find(1) == count_to_dll.end()) count_to_dll[1] = new DLL();
            DLL* dll = count_to_dll[1];
            dll->emplace(node);
            min_count = 1;
            ++size;
        } else {
            Node* node = key_to_node[key];
            node->value = value;
            int count = key_to_count[key];
            DLL* dll = count_to_dll[count];
            dll->erase(node);
            if(dll->size() == 0 && min_count == count) ++min_count;
            if(count_to_dll.find(count+1) == count_to_dll.end()) count_to_dll[count+1] = new DLL();
            dll = count_to_dll[count+1];
            
            dll->emplace(node);
            key_to_count[key] = count + 1;
        }
    }
};

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache* obj = new LFUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
