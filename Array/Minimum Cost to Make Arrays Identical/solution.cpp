class Solution {
public:
    long long minCost(vector<int>& arr, vector<int>& brr, long long k) {
        int n = arr.size();
        long long res1{}, res2{k};
        // subtract/add
        for(int i{}; i < n; ++i) {
            res1 += abs(arr[i] - brr[i]);
        }
        sort(arr.begin(), arr.end());
        sort(brr.begin(), brr.end());
        for(int i{}; i < n; ++i) {
            res2 += abs(arr[i] - brr[i]);
        }
        // sort -> subtract/add
        return min(res1, res2);
    }
};
