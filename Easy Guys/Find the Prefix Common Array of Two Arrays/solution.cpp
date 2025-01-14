class Solution {
public:
    vector<int> findThePrefixCommonArray(vector<int>& A, vector<int>& B) {
        int n = A.size();
        vector<int> C(n);
        vector<int> counter(n+1);
        int common{};
        for(int i{}; i < n; ++i) {
            counter[A[i]]++;
            if(counter[A[i]] == 2) ++common; 
            counter[B[i]]++;
            if(counter[B[i]] == 2) ++common;
            C[i] = common;
        }
        return C;
        
    }
};
