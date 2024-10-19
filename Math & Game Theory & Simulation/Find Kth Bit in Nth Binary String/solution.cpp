class Solution {
public:
    char findKthBit(int n, int k) {
        int l = 1;
        for(int i = 2; i <= n; ++i) {
            l = l * 2 + 1;
        }
        --k;
        int flip = 0;
        while(l > 1) {
            if(k == l/2) return flip & 1 ? '0' : '1';
            if(k > l/2) {
                int d = k-(l/2+1);
                k = l/2-1-d;
                flip ^= 1;
            }
            l = (l-1)/2;
        }
        if(flip & 1) return '1';
        return '0';
    }
};
