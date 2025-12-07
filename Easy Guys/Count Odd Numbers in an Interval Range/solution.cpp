class Solution {
public:
    int countOdds(int low, int high) {
        return (high - low) / 2 + 1 - (((low|high)&1) == 0);
    }
};
