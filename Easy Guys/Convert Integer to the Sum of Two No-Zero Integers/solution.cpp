class Solution {
public:
    vector<int> getNoZeroIntegers(int n) {
        auto contain_zero = [](int n) {
            while(n) {
                if(n % 10 == 0) return true;
                n /= 10;
            }
            return false;
        };
        for(int a = 1; a < n; ++a) {
            int b = n-a;
            if(!contain_zero(a) && !contain_zero(b)) return {a, b};
        }
        return {};
    }
};
