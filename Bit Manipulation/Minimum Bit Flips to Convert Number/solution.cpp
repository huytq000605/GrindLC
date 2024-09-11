class Solution {
public:
    int minBitFlips(int start, int goal) {
        int result = 0;
        int cur = start ^ goal;
        while(cur) {
            result += cur & 1;
            cur >>= 1;
        }
        return result;
    }
};
