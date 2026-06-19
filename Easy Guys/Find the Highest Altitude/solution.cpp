class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int result = 0;
        int cur = 0;
        for(auto g: gain) {
            cur += g;
            result = max(result, cur);
        }
        return result;
    }
};
