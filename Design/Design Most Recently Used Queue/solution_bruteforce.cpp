class MRUQueue {
vector<int> vec;
public:
    MRUQueue(int n) {
        vec.resize(n);
        for(int i{}; i < n; ++i) vec[i] = i+1;
    }
    
    int fetch(int k) {
        k -= 1;
        int target = vec[k];
        for(int i{k}; i < vec.size()-1; i++) {
            vec[i] = vec[i+1];
        }
        vec.back() = target;
        return target;
    }
};

/**
 * Your MRUQueue object will be instantiated and called as such:
 * MRUQueue* obj = new MRUQueue(n);
 * int param_1 = obj->fetch(k);
 */
