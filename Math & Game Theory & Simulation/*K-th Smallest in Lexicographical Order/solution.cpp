class Solution {
public:
    int findKthNumber(int n, int k) {
        //                 1
        //       /       /    \   \  ... \
        //      0       1     2    3 ...  9
        //     /...\   /...\  ....
        //    0 ... 9  0...9  ...
        // Steps between 2 consecutive nodes in the same level are
        // the number of nodes on the left subtree
        auto steps = [&n](long long n1, long long n2) {
            int result = 0;
            while(n1 <= n) {
                result += min(static_cast<long long>(n+1), n2) - n1;
                n1 *= 10;
                n2 *= 10;
            }
            return result;
        };
        int cur = 1;
        k -= 1;
        while(k) {
            int s = steps(cur, cur+1);
            if(s <= k) {
                k -= s;
                cur += 1;
            } else {
                cur *= 10;
                k -= 1;
            } 
        }
        return cur;
    }
};
