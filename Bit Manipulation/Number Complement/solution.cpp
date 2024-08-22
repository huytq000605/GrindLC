class Solution {
public:
    int findComplement(int num) {
        int result = 0;
        int bit = 0;
        while(num) {
            result |= (1 - (num & 1)) << bit;
            num >>= 1;
            bit++;
        }
        return result;
    }
};
