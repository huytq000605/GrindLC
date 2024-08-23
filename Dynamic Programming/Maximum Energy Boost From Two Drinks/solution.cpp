class Solution {
public:
    long long maxEnergyBoost(vector<int>& A, vector<int>& B) {
        long long lastA = A[0], lastB = B[0];
        int n = A.size();
        for(int i = 1; i < n; ++i) {
            long long next_lastA = max(lastA + A[i], lastB);
            long long next_lastB = max(lastB + B[i], lastA);
            swap(lastA, next_lastA);
            swap(lastB, next_lastB);
        }
        return max(lastA, lastB);
    }
};
