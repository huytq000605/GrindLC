class Solution {
public:
    int maximumElementAfterDecrementingAndRearranging(vector<int>& arr) {
        int n = arr.size();
        int m = min(*max_element(begin(arr), end(arr)), n);
        vector<int> freq(m + 1);
        for(int num: arr) freq[min(num, m)] += 1;
        int result = 0;
        for(int i = 1; i <= m; ++i) {
            result = min(result + freq[i], i);
        }
        return result;
    }
};
