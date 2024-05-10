class Solution {
public:
    vector<int> kthSmallestPrimeFraction(vector<int>& arr, int k) {
        int n = arr.size();
        priority_queue<tuple<double, int, int>, vector<tuple<double, int, int>>, 
        decltype([](tuple<double, int, int> a, tuple<double, int, int> b) {
            return get<0>(a) > get<0>(b);  
        })> pq;
        for(int i = 0; i < n-1; i++) {
            pq.emplace(double(arr[i]) / arr[n-1], i, n-1);
        }
        vector<int> result(2);
        while(k--) {
            auto [v, i, j] = pq.top();
            result[0] = arr[i];
            result[1] = arr[j];
            pq.pop();
            if(j-1 > i) {
                pq.emplace(double(arr[i]) / arr[j-1], i, j-1);
            }
        }
        return result;
    }
};
