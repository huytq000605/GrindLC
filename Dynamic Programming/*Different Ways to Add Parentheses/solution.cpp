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

        auto dfs = [&](int i, int j, auto dfs_ref) -> vector<int> {
            if(i == j) return {nums[i]};
            vector<int> result;
            for(int k = i; k < j; ++k) {
                auto vs1 = dfs_ref(i, k, dfs_ref);
                auto vs2 = dfs_ref(k+1, j, dfs_ref);
                for(auto v1: vs1) {
                    for(auto v2: vs2) {
                        int v;
                        switch(ops[k]) {
                            case '+':
                                v = v1 + v2;
                                break;
                            case '-':
                                v = v1 - v2;
                                break;
                            case '*':
                                v = v1 * v2;
                                break;
                        }
                        result.emplace_back(v);
                    }
                }
            }

            return result;
        };

        return dfs(0, nums.size() - 1, dfs);
    }
};
