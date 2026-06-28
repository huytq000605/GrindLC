class Solution {
public:
    int maximumElementAfterDecrementingAndRearranging(vector<int>& arr) {
        sort(begin(arr), end(arr));
        int prev = 0;
        int result = 0;
        for(int num: arr) {
            num = min(prev+1, num);
            result = max(result, num);
            prev = num;
        }
        return result;
    }
};
