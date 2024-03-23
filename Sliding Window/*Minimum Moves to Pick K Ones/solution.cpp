class Solution {
public:
    long long ZERO = 0; // Cast 0 constant to long long
    long long minimumMoves(vector<int>& nums, long long k, long long maxChanges) {
        std::vector<long long> one_indexes;
        for(int i = 0; i < nums.size(); i++) {
            if(nums[i] == 1) one_indexes.push_back(i);
        }
        if(one_indexes.size() == 0) return k * 2;

        std::vector<long long> prefix(one_indexes.size());
        for(int i = 0; i < one_indexes.size(); i++) {
            if(i > 0) prefix[i] = prefix[i-1];
            prefix[i] += one_indexes[i];
        }
        long long result = 1e18;
        long long min_step2 = k - 1 - maxChanges;
        
        min_step2 = std::max(ZERO, min_step2);
        for(long long step2 = min_step2; step2 < min_step2 + 3 && step2 <= k && step2 <= one_indexes.size(); step2++) {
            long long step1 = std::max(ZERO, k - 1 - step2);
            for(int left = 0; left < one_indexes.size() - step2; left++) {
                // right - left + 1 = step2 + 1
                int right = step2 + left;
                int median = (left + right) / 2;
                long long res = (prefix[right] - (median > 0 ? prefix[median-1] : 0)) - one_indexes[median] * (right - median + 1);
                res += one_indexes[median] * (median - left + 1) - (prefix[median] - (left > 0 ? prefix[left-1]: 0));
                res += step1 * 2;
                result = std::min(result, res);
            }
        }
        return result;
    }
};
