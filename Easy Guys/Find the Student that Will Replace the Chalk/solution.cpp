class Solution {
public:
    int chalkReplacer(vector<int>& chalk, int k) {
        long long s = accumulate(chalk.begin(), chalk.end(), static_cast<long long>(0));
        k %= s;
        for(int i = 0; i < chalk.size(); i++) {
            if(k < chalk[i]) return i;
            k -= chalk[i];
        }
        return -1;
    }
};
