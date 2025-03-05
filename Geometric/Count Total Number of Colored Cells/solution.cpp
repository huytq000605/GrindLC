class Solution {
public:
    long long coloredCells(int n) {
        long long result{1};
        for(long long i{1}; i < n; ++i) {
            result += 4*i;
        }
        return result;
    }
};
