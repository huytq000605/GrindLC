class Solution {
public:
    long long f(int n) {
        if(n == 0) return 1;
        return n * f(n-1);
    }
    long long countGoodIntegers(int n, int k) {
        int m = (n+1)/2;
        int mn = pow(10, m-1);
        int mx = pow(10, m) - 1;
        long long result = 0;
        set<string> seen;
        // Loop through all the palindrome
        for(int half = mn; half <= mx; ++half) {
            string half_str = to_string(half);
            reverse(half_str.begin(), half_str.end());
            long long palindrome = half;
            for(int i = n % 2; i < half_str.size(); i++) {
                palindrome = palindrome * 10 + (half_str[i] - '0');
            }
            if(palindrome % k) continue;
            // Avoid same set of digits from different palindromes
            string key = to_string(palindrome);
            sort(key.begin(), key.end());
            if(seen.find(key) != seen.end()) continue;
            seen.emplace(key);
            map<int, int> counter;
            while(palindrome) {
                counter[palindrome % 10] += 1;
                palindrome /= 10;
            }
            // First digit cannot be 0
            long long comb = (n - counter[0]) * f(n-1);
            // Remove duplicate numbers by swapping same digits
            for(auto it: counter) {
                if(!it.second) continue;
                comb /= f(it.second);
            }
            result += comb;
        }
        return result;
    }
};
