class Solution {
public:
    vector<int> diffWaysToCompute(string expression) {
        vector<char> ops = {};
        vector<int> nums = {};
        int num = 0;
        for(char c: expression) {
            if(c == '+' || c == '-' || c == '*') {
                nums.emplace_back(num);
                num = 0;
                ops.emplace_back(c);
            } else {
                num = num*10 + c - '0';
            }
        }
        nums.emplace_back(num);
        int n = nums.size();
        vector<vector<vector<int>>> dp(n, vector<vector<int>>(n, vector<int>()));
        for(int i = 0; i < n; ++i) dp[i][i] = {nums[i]};
        for(int l = 2; l <= n; ++l) {
            for(int i = 0; i <= n-l; ++i) {
                int j = i+l-1;  
                for(int k = i; k < j; ++k) {
                    vector<int>& lefts = dp[i][k];
                    cout << lefts.size() << endl;
                    vector<int>& rights = dp[k+1][j];
                    cout << rights.size() << endl;
                    vector<int>& merge = dp[i][j];
                    for(int left: lefts) {
                        for(int right: rights) {
                            cout << left << " " << right << endl;
                            if(ops[k] == '+') merge.emplace_back(left + right);
                            else if(ops[k] == '-') merge.emplace_back(left - right);
                            else merge.emplace_back(left * right);
                        }
                    }
                    
                }
            }
        }
        return dp[0][n-1];
    }
};
