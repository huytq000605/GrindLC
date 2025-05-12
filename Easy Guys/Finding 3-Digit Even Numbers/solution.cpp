class Solution {
public:
    vector<int> findEvenNumbers(vector<int>& digits) {
        vector<int> counter(10);
        for(int d: digits) counter[d]++;
        vector<int> result;
        for(int d1 = 1; d1 <= 9; ++d1) {
            if(!counter[d1]) continue;
            counter[d1]--;
            for(int d2 = 0; d2 <= 9; ++d2) {
                if(!counter[d2]) continue;
                counter[d2]--;
                for(int d3 = 0; d3 <= 9; d3 += 2) {
                    if(!counter[d3]) continue;
                    result.emplace_back(d1 * 100 + d2 * 10 + d3);
                }
                counter[d2]++;
            }
            counter[d1]++;
        }
        return result;
    }
};
