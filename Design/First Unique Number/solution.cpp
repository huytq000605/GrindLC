class FirstUnique {
std::deque<int> dq{};
std::unordered_map<int, int> um{};
public:
    FirstUnique(vector<int>& nums) {
        dq = std::deque<int>(nums.begin(), nums.end());
        for(int num: nums) ++um[num];
    }
    
    int showFirstUnique() {
        while(!dq.empty() && um[dq.front()] > 1) dq.pop_front();
        if(dq.empty()) return -1;
        return dq.front();
    }
    
    void add(int value) {
        ++um[value];
        if(um[value] > 1) return;
        dq.emplace_back(value);
    }
};

/**
 * Your FirstUnique object will be instantiated and called as such:
 * FirstUnique* obj = new FirstUnique(nums);
 * int param_1 = obj->showFirstUnique();
 * obj->add(value);
 */
