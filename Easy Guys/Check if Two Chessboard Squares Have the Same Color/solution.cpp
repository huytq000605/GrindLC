class Solution {
public:
    bool checkTwoChessboards(string coordinate1, string coordinate2) {
        int rd = abs(coordinate1[0] - coordinate2[0]) % 2;
        int cd = abs(coordinate1[1] - coordinate2[1]) % 2;
        return rd == 0 ? cd == 0 : cd == 1;
    }
};
