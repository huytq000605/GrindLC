class Solution {
public:
    int minSumOfLengths(vector<int>& arr, int target) {
        vector<int> prefix(arr.size(), INT_MAX);
        int s = 0;
        for(int i = 0, j = 0; i < arr.size(); ++i) {
            if(i) prefix[i] = prefix[i-1];
            s += arr[i];
            while(s > target) {
                s -= arr[j++];
            }
            if(s == target) prefix[i] = min(prefix[i], i - j + 1);
        }
        s = 0;
        int result = INT_MAX;
        for(int i = arr.size()-1, j = arr.size() - 1; i > 0; --i) {
            if(prefix[i-1] == INT_MAX) break;
            s += arr[i];
            while(s > target) {
                s -= arr[j--];
            }
            if(s == target) result = min(result, j - i + 1 + prefix[i-1]);
            
        }
        return result == INT_MAX ? -1: result;
    }
};
