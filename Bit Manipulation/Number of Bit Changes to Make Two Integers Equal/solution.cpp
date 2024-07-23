class Solution {
public:
    int minChanges(int n, int k) {
        int result = 0;
        while(n > k) {
            if(k&1) {
                if(!(n&1)) return -1;
            } else {
                if(n & 1) result++;
            }
            n >>= 1;
            k >>= 1;
        }
        return n == k ? result : -1; 
    }
};
