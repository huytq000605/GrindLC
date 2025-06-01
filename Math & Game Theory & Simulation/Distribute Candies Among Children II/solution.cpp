class Solution {
public:
    long long distributeCandies(int n, int limit) {
        long long result = 0;
        for(long long first = max(n - 2 * limit, 0); first <= min(n, limit); ++first) {
            long long remaining = n - first;
            long long min_second = max(0ll, remaining - limit);
            long long max_second = min(remaining, static_cast<long long>(limit));
            result += max_second - min_second + 1;
        }
        return result;
    }
};
