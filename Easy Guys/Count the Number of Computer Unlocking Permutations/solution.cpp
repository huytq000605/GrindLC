class Solution {
public:
    int countPermutations(vector<int>& complexity) {
        int MOD = 1e9 + 7;
        int result = 1;
        for(int i = 1; i < complexity.size(); ++i) {
            if(complexity[i] <= complexity[0]) return 0;
            result = (1LL * result * i) % MOD;
        }
        return result;
    }
};
