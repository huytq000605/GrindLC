class NumberContainers {
public:
unordered_map<int, priority_queue<int, vector<int>, greater<int>>> m;
unordered_map<int, int> nums;
    NumberContainers() {
        
    }
    
    void change(int index, int number) {
        nums[index] = number;
        m[number].emplace(index);
    }
    
    int find(int number) {
        if(m.find(number) == m.end()) return -1;
        while(!m[number].empty()) {
            int idx = m[number].top();
            if(nums[idx] != number) {
                m[number].pop();
            } else {
                return idx;
            }
        }
        return -1;
    }
};

/**
 * Your NumberContainers object will be instantiated and called as such:
 * NumberContainers* obj = new NumberContainers();
 * obj->change(index,number);
 * int param_2 = obj->find(number);
 */
