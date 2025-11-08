class Solution {
public:
    int minimumOneBitOperations(int n) {
        if(n <= 1) return n;
        int msb = 0;
        for(int i = 30; i >= 0; --i) {
            if((n >> i) & 1) {
                msb = i;
                break;
            }   
        }
        // 1000
        // 1001
        // 1011
        // 1010
        // 1110
        // 1111
        // 1101
        // 1100
        // 100
        // 101
        // 111
        // 110
        // 10
        // 11
        // 1
        // 0
        // -------------------------
        // 2^k -> 0 = 2^(k-1) -> 0 + (1 << k)
        //          = (1 << k) + (1 << (k-1)) + ... 1
        //          = (1 << (k+1)) - 1
        return (1 << (msb+1)) - 1 - minimumOneBitOperations((~(1 << msb)) & n);
    }
};
