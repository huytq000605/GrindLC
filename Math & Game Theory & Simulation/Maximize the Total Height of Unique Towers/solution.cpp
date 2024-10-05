class Solution {
public:
    long long maximumTotalSum(vector<int>& A) {
        sort(A.begin(), A.end());
        int v = A.back();
        long long result = 0;
        for(int i = A.size() - 1; i >= 0; --i) {
            if(v == 0) return -1;
            v = min(v, A[i]);
            result += v;
            --v;
        }
        return result;
    }
};
