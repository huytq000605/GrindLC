class Solution {
public:
    vector<bool> prefixesDivBy5(vector<int>& nums) {
        vector<bool> result;
        int mod = 0;
        for(int num: nums) {
            mod = ((mod << 1) | num) % 5;
            if(!mod) result.push_back(true);
            else result.push_back(false);
        }
        return result;
    }
};
