class Solution {
static constexpr int MOD = 1000000007;
using Matrix = vector<vector<long long>>;
Matrix mul(const Matrix& A, const Matrix& B) {
    Matrix C(A.size(), vector<long long>(B[0].size(), 0));
    for(int i = 0; i < A.size(); ++i) {
        for(int j = 0; j < B[0].size(); ++j) {
            for(int k = 0; k < B.size(); ++k) {
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD;
            }
        }
    }
    return C;
}

Matrix pow(Matrix A, int exp) {
    if(exp == 1) return A;
    Matrix res = pow(A, exp/2);
    res = mul(res, res);
    return exp & 1 ? mul(A, res) : res;
}
public:
    int lengthAfterTransformations(string s, int t, vector<int>& nums) {
        Matrix m(26, vector<long long>(26, 0));
        for(int i = 0; i < 26; ++i) {
            for(int j = 1; j <= nums[i]; ++j) {
                m[i][(i+j)%26] = 1;
            }
        }
        Matrix e = pow(m, t);
        Matrix counter(1, vector<long long>(26, 0));
        for(char c: s) ++counter[0][c - 'a'];
        Matrix res = mul(counter, e);
        int result = 0;
        for(int i = 0; i < 26; ++i) result = (result + res[0][i]) % MOD;
        return result; 
    }
};
