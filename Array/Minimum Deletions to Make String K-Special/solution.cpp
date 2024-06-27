class Solution {
public:
    int minimumDeletions(string word, int k) {
        std::vector<int> counter(26);
        for(auto &c: word) {
            counter[c - 'a'] += 1;
        }
        int result = 1e5;
        for(auto &target: counter) {
            if(!target) continue;
            int res = 0;
            for(auto &freq: counter) {
                if(!freq) continue;
                res += (freq < target) ? freq : max(0, freq - target - k);
            }
            result = min(result, res);
        }
        return result;
    }
};
