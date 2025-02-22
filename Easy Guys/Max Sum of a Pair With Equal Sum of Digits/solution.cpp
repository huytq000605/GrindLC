class Solution {
public:
    int maximumSum(vector<int>& nums) {
        int result{-1};
        unordered_map<int, int> m;
        for(auto num: nums) {
            int s{};
            for(int cur{num}; cur > 0; cur /= 10)
                s += cur % 10;
            if(m.find(s) != m.end()) result = max(result, m[s] + num);
            m[s] = max(m[s], num);
        }
        return result;
    }
};
