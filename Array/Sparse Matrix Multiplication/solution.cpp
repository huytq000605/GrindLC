class Solution {
public:
    vector<vector<int>> multiply(vector<vector<int>>& mat1, vector<vector<int>>& mat2) {
        // m*n * n*p = m*p
        int m = mat1.size(), n = mat1[0].size(), p = mat2[0].size();

        vector<vector<int>> result(m, vector<int>(p));
        vector<vector<int>> A(m), B(p);
        for(int i = 0; i < m; ++i) {
            for(int j = 0; j < n; ++j) {
                if(mat1[i][j]) A[i].emplace_back(j);
            }
        }
        for(int i = 0; i < p; ++i) {
            for(int j = 0; j < n; ++j) {
                if(mat2[j][i]) B[i].emplace_back(j);
            }
        }

        for(int i = 0; i < m; ++i) {
            for(int j = 0; j < p; ++j) {
                int a = 0, b = 0;
                while(a < A[i].size() && b < B[j].size()) {
                    if(A[i][a] == B[j][b]) {
                        result[i][j] += mat1[i][A[i][a++]] * mat2[B[j][b++]][j];
                    } else if(A[i][a] < B[j][b]) {
                        ++a;
                    } else {
                        ++b;
                    }
                }
            }
        }
        return result;
    }
};
