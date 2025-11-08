class TwoSum {
unordered_set<int> num;
unordered_set<int> sum;
public:
    TwoSum() {
        
    }
    
    void add(int number) {
        for(int n: num) {
            sum.insert(n + number);
        }
        num.insert(number);
    }
    
    bool find(int value) {
        return sum.contains(value);
    }
};

/**
 * Your TwoSum object will be instantiated and called as such:
 * TwoSum* obj = new TwoSum();
 * obj->add(number);
 * bool param_2 = obj->find(value);
 */
