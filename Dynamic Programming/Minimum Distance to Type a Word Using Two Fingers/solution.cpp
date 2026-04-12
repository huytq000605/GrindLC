class Solution {
    int distance(int a, int b) {
        int r1 = a / 6, c1 = a % 6;
        int r2 = b / 6, c2 = b % 6;
        if(a == 26 || b == 26) return 0;
        return abs(r1 - r2) + abs(c1 - c2);
    }
public:
    int minimumDistance(string word) {
        vector<int> dp(27, INT_MAX);
        dp[26] = 0;
        for(int i = 1; i < word.size(); ++i) {
            vector<int> ndp(27, INT_MAX);
            int c = word[i] - 'A';
            int pc = word[i-1] - 'A';

          
            for(int prev = 0; prev <= 26; ++prev) {
                // finger holds at prev and pc
                if(dp[prev] == INT_MAX) continue;
                
                // change the finger holds at pc
                ndp[prev] = min(ndp[prev], distance(pc, c) + dp[prev]);

                // change the finger holds at prev
                ndp[pc] = min(ndp[pc], distance(prev, c) + dp[prev]); 
            }

            
            dp = ndp;
        }
        return *min_element(begin(dp), end(dp));
        
    }
};
