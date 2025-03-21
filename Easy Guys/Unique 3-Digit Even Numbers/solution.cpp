class Solution {
public:
    int totalNumbers(vector<int>& digits) {
        int n = digits.size();
        unordered_set<int> seen;
        for(int i{}; i < n; ++i) {
            if(digits[i] == 0) continue;
            for(int j{}; j < n; ++j) {
                if(i == j) continue;
                for(int k{}; k < n; ++k) {
                    if(i == k || j == k || digits[k] & 1) continue;
                    int num = digits[i] * 100 + digits[j] * 10 + digits[k];
                    seen.emplace(num);
                }
            }
        }
        return seen.size();
    }
};
