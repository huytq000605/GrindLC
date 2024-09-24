class Solution {
public:
    int longestCommonPrefix(vector<int>& arr1, vector<int>& arr2) {
        unordered_set<int> s;
        for(int num: arr1) {
            int divisor = 1;
            while(num / divisor >= 10) {
                divisor *= 10;
            }
            int cur = 0;
            for(; divisor > 0; divisor /= 10) {
                cur = cur * 10 + (num / divisor) % 10;
                s.emplace(cur);
            }
        }

        int result = 0;
        for(int num: arr2) {
            int divisor = 1;
            while(num / divisor >= 10) {
                divisor *= 10;
            }
            int i = 0;
            int cur = 0;
            for(; divisor > 0; divisor /= 10) {
                cur = cur * 10 + (num / divisor) % 10;
                if(s.find(cur) == s.end()) break;
                result = max(result, ++i);
            }
        }
        return result;
    }
};
