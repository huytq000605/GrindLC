class Solution {
public:
    string smallestNumber(string num, long long t) {
        // return -1 if t has factor that is not in {2,3,5,7}
        // due to max(digit) = 9
        auto tc = t;
        for(int i: {2,3,5,7}) {
            while(tc % i == 0) tc /= i;
        }
        if(tc != 1) return "-1";
        
        // ts[i] = remaining product of digits after i digit
        int n = num.size();
        // m is the index of first 0 in num else last index of num 
        int m = n-1;
        vector<long long> ts(n+1, t);
        for(int i{}; i < n; ++i) {
            if(num[i] == '0') {
                m = i;
                break;
            }
            ts[i+1] = ts[i] / gcd(ts[i], num[i] - '0');
        }
        if(ts.back() == 1) return num;

        // return zero-free number where product of its digit
        // divisible by t, and has length of at least n
        auto fill = [](long long t, int n) {
            string result;
            for(int i = 9; i > 1; --i) {
                while(t % i == 0) {
                    result += (i + '0');
                    t /= i;
                    --n;
                }
            }
            while(n-- > 0) result += '1';
            reverse(result.begin(), result.end());
            return result;
        };

        // try to increase at i, and fill what ever on the right
        // right is valid if length(right) = right_digits
        for(int i{m}; i >= 0; --i) {
            int right_digits = n-1-i;
            long long t = ts[i];
            for(int d = num[i] - '0' + 1; d < 10; ++d) {
                string right = fill(t / gcd(t, d), right_digits);
                // cout << i << " " << d << " " << rights << endl;
                if(right.size() == right_digits)
                    return num.substr(0, i) + string(1, d + '0') + right;
            }
        }
        return fill(t, n+1);
    }
};
