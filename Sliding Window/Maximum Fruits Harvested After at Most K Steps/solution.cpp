class Solution {
public:
    int maxTotalFruits(vector<vector<int>>& fruits, int start, int k) {
        int result = 0;
        int n = fruits.size();
        auto cal = [&]() {
            int cur = 0;
            for(int i = 0, j = 0; i < n; ++i) {
                int p = fruits[i][0];
                int a = fruits[i][1];
                if(p > start + k) break;
                cur += a;
                if(p >= start) {
                    int remaining = k - 2 * (p - start);
                    while(fruits[j][0] < start && start - fruits[j][0] > remaining) {
                        cur -= fruits[j][1];
                        ++j;
                    }
                    result = max(result, cur);
                }
            }
        };

        cal();
        for(int i = 0; i < (n >> 1); ++i) {
            fruits[i][0] = -fruits[i][0];
            fruits[n-1-i][0] = -fruits[n-1-i][0];
            swap(fruits[i], fruits[n-1-i]);
        }
        if(n & 1) fruits[n >> 1][0] = -fruits[n >> 1][0];
        start = -start;
        cal();
        return result;
    }
};
