class Solution {
public:
    int findLHS(vector<int>& nums) {
        unordered_map<int, int> counter;
        for(int num: nums) {
            counter[num] += 1;
        }
        int result = 0;
        for(auto &[num, freq]: counter) {
            if(counter.find(num+1) != counter.end()) {
                int freq2 = counter[num+1];
                result = max(result, freq + freq2);
            }
        }
        return result;
    }
};
