class Solution {
public:
    int minHeightShelves(vector<vector<int>>& books, int shelfWidth) {
        int n = books.size();
        vector<int> dp(n+1, INT_MAX);
        dp[0] = 0;
        for(int i = 0; i < n; i++) {
            int w = books[i][0], h = books[i][1];
            dp[i+1] = dp[i] + h;
            for(int j = i-1; j >= 0; j--) {
                w += books[j][0];
                h = max(h, books[j][1]);
                if(w > shelfWidth) break;
                dp[i+1] = min(dp[i+1], dp[j] + h);
            }
        }
        return dp[n];
    }
};
