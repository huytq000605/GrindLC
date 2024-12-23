class Solution {
public:
    int makeStringGood(string s) {
        int mx{};
        unordered_map<int, int> counter;
        for(char c: s) {
            counter[c-'a']++;
            mx = max(mx, counter[c-'a']);
        }
        int result{INT_MAX};
        for(int target{}; target <= mx; ++target) {
            map<pair<int, int>, int> memo;
            function<int(int, int)> dfs = [&](int i, int deleted) {
                if(i >= 26) return 0;
                if(memo.find({i, deleted}) != memo.end()) return memo[{i, deleted}];
                int result{};
                if(counter[i] < target) {
                    result = dfs(i+1, counter[i]) + counter[i];
                    int increase{target - counter[i]};
                    result = min(result, dfs(i+1, 0) + max(0, increase - deleted));
                } else {
                    result = dfs(i+1, counter[i] - target) + (counter[i] - target);
                }
                memo[{i, deleted}] = result;
                return result;
            };
            result = min(result, dfs(0, 0));
        }
        return result;
    }
};
