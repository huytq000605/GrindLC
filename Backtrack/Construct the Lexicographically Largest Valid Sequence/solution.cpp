class Solution {
public:
    vector<int> constructDistancedSequence(int n) {
        vector<int> nums(n);
        for(int i{}; i < n; ++i) {
            nums[i] = n-i;
        }
        vector<int> result(n*2-1);
        auto dfs = [&](this auto& dfs, int i) {
            if(i >= result.size()) return true;
            if(result[i]) return dfs(i+1);
            for(int j{}; j < n; ++j) {
                int num = nums[j];
                if(!num) continue;
                if(num != 1 && (i + num >= n*2-1 || result[i+num])) continue;
                nums[j] = 0;
                result[i] = num;
                if(num != 1) result[i+num] = num;
                if(dfs(i+1)) return true;
                nums[j] = num;
                result[i] = 0;
                if(num != 1) result[i+num] = 0;
            }
            return false;
        };
        dfs(0);
        return result;
    }
};
