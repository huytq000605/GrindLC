class Solution {
public:
    int findMaxK(vector<int>& nums) {
        set<int> seen;
        int result = -1;
        for(int num : nums) {
            seen.emplace(num);
            if(seen.find(num) != seen.end() && seen.find(-num) != seen.end()) {
                result = max(result, abs(num));
            }
        }
        return result;
    }
};
