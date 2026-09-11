class Solution {
public:
    int totalNumbers(vector<int>& digits) {
        int result = 0;
        vector<int> counter(10);
        for(int d: digits) counter[d]++;
        for(int d3 = 0; d3 < 10; d3 += 2) {
            if(!counter[d3]) continue;
            counter[d3]--;
            for(int d2 = 0; d2 < 10; ++d2) {
                if(!counter[d2]) continue;
                counter[d2]--;
                for(int d1 = 1; d1 < 10; ++d1) {
                    if(!counter[d1]) continue;
                    result += 1;
                }
                counter[d2]++;
            }
            counter[d3]++;
        }
        return result;
    }
};
