class Solution {
public:
    int maxFrequencyElements(vector<int>& nums) {
        vector<int> freq(101);
        for(int num: nums) freq[num]++;
        int max_freq = *max_element(freq.begin(), freq.end());
        int result = 0;
        for(int num: nums) if(freq[num] == max_freq) ++result;
        return result;
    }
};
