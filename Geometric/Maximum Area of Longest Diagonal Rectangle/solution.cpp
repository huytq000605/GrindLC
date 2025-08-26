class Solution {
public:
    int areaOfMaxDiagonal(vector<vector<int>>& dimensions) {
        int result = 0;
        int max_dia = 0;
        for(auto &d: dimensions) {
            int dia = d[0] * d[0] + d[1] * d[1];
            cout << dia << endl;
            if(dia > max_dia) {
                result = d[0] * d[1];
                max_dia = dia;
            } else if(dia == max_dia) {
                result = max(result, d[0] * d[1]);
            }
        }
        return result;
    }
};
