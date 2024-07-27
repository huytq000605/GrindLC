class Solution {
public:
    int minOperations(vector<int>& nums) {
        vector<int> states;
        for(auto num: nums) {
            if(states.empty() || states.back() >= num) {
                states.emplace_back(num);
            } else {
                auto i = upper_bound(states.begin(), states.end(), num, [](int a, int b) {
                    return a > b;
                });
                *i = num;
            }
        }
        return states.size();
    }
};
