class Solution {
public:
    vector<int> decrypt(vector<int>& code, int k) {
        int n = code.size();
        vector<int> result(n, 0);
        int s{}, start{1}, end{k};
        if(k < 0) {
            k = -k;
            start = n-k;
            end = n-1;
        }
        for(int i{start}; i <= end; ++i) s += code[i];
        for(int i{}; i < n; ++i) {
            result[i] = s;
            s -= code[(start++)%n];
            s += code[(++end)%n];
        }
        return result;
    }
};
