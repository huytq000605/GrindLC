class Solution {
public:
    long long maxRunTime(int n, vector<int>& batteries) {
        sort(batteries.begin(), batteries.end());
        long long s = accumulate(batteries.begin(), batteries.end(), 0ll);
        int i = batteries.size() - 1;
        while(n > 1 && batteries[i] > s / n) {
            n -= 1;
            s -= batteries[i];
            --i;
        }
        return s / n;
    }
};
