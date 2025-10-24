class Solution {
public:
    int nextBeautifulNumber(int n) {
        auto is_balance = [](int n) -> bool {
            vector<int> counter(10);
            while(n) {
                ++counter[n % 10];
                n /= 10;
            }
            for(int c = 0; c < 10; ++c) {
                if(counter[c] && counter[c] != c) return false;
            }
            return true;
        };
        for(int num = n+1; num <= 1224444; ++num) {
            if(is_balance(num)) return num;
        }
        return -1;
    }
};
