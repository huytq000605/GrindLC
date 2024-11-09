class Solution {
public:
    long long minEnd(int n, int x) {
        --n;
        long long result = x;
        for(long long bit{1}; n; bit <<= 1) {
            if(result & bit) continue;
            if(n & 1) result |= bit;
            n >>= 1;
        }
        return result;
    }
};
