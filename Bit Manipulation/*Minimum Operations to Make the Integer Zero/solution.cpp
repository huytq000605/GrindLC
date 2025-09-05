class Solution {
public:
    int makeTheIntegerZero(int num1, int num2) {
        for(long long op = 1; op <= 60; ++op) {
            long long target = num1 - 1LL * num2 * op;
            long long bit_count = __builtin_popcountll(target);
            // we need at least operation = bit count
            // we could only have at most operation = target
            if(bit_count <= op && op <= target) {
                return op;
            }
        }
        return -1;
    }
};
