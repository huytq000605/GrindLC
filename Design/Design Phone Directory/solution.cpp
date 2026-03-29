class PhoneDirectory {
vector<int> nums;
unordered_set<int> used;
public:
    PhoneDirectory(int maxNumbers) {
        for(int i = 0; i < maxNumbers; ++i) {
            nums.push_back(i);
        }
    }
    
    int get() {
        if(nums.empty()) return -1;
        
        int num = nums.back();
        used.insert(num);
        nums.pop_back();
        return num;
    }
    
    bool check(int number) {
        if(used.find(number) != used.end()) return false;
        return true;
    }
    
    void release(int number) {
        if(used.find(number) == used.end()) return;
        used.erase(number);
        nums.push_back(number);
    }
};

/**
 * Your PhoneDirectory object will be instantiated and called as such:
 * PhoneDirectory* obj = new PhoneDirectory(maxNumbers);
 * int param_1 = obj->get();
 * bool param_2 = obj->check(number);
 * obj->release(number);
 */
