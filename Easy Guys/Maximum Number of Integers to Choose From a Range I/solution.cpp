class Solution {
public:
    int maxCount(vector<int>& banned, int n, int maxSum) {
        vector<int> ban(n+1, 0);
        for(int b: banned) {
            if(b > n) continue;
            ban[b] = 1;
        }
        int s{};
        int result{};
        for(int i{1}; i <= n; ++i) {
            if(ban[i]) continue;
            if(s + i > maxSum) break;
            s += i;
            ++result;
        }
        return result;
    }
};
