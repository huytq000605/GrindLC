class CustomStack {
int cap;
stack<int> s;
vector<int> incr;
public:
    CustomStack(int maxSize) {
        cap = maxSize;
    }
    
    void push(int x) {
        if(s.size() == cap) return;
        s.emplace(x);
        incr.emplace_back(0);
    }
    
    int pop() {
        int i = s.size() - 1;
        if(i < 0) return -1;
        int d = incr[i];
        if(i > 0) incr[i-1] += d;
        incr.pop_back();
        int res = s.top();
        s.pop();
        return res + d;
    }
    
    void increment(int k, int val) {
        if(s.size() == 0) return;
        incr[min(int(s.size()) - 1, k-1)] += val;
    }
};

/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack* obj = new CustomStack(maxSize);
 * obj->push(x);
 * int param_2 = obj->pop();
 * obj->increment(k,val);
 */
