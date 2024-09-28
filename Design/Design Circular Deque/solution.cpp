class MyCircularDeque {
int cap, size, i, j;
vector<int> arr;
public:
    MyCircularDeque(int k) {
        cap = k;
        i = cap-1;
        size = j = 0;
        arr.resize(k);
    }
    
    bool insertFront(int value) {
        if(size == cap) return false;
        arr[i] = value;
        i = (i-1+cap)%cap;
        ++size;
        return true;
    }
    
    bool insertLast(int value) {
        if(size == cap) return false;
        arr[j] = value;
        j = (j+1)%cap;
        ++size;
        return true;
    }
    
    bool deleteFront() {
        if(size == 0) return false;
        i = (i+1) % cap;
        --size;
        return true;
    }
    
    bool deleteLast() {
        if(size == 0) return false;
        j = (j-1+cap) % cap;
        --size;
        return true;
    }
    
    int getFront() {
        if(size == 0) return -1;
        return arr[(i+1)%cap];
    }
    
    int getRear() {
        if(size == 0) return -1;
        return arr[(j-1+cap)%cap];
    }
    
    bool isEmpty() {
        return size == 0;
    }
    
    bool isFull() {
        return size == cap;
    }
};

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * MyCircularDeque* obj = new MyCircularDeque(k);
 * bool param_1 = obj->insertFront(value);
 * bool param_2 = obj->insertLast(value);
 * bool param_3 = obj->deleteFront();
 * bool param_4 = obj->deleteLast();
 * int param_5 = obj->getFront();
 * int param_6 = obj->getRear();
 * bool param_7 = obj->isEmpty();
 * bool param_8 = obj->isFull();
 */
