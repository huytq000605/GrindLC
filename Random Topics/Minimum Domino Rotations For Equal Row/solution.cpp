class Solution {
public:
    int minDominoRotations(vector<int>& tops, vector<int>& bottoms) {
        int n = tops.size();
        for(int target: {tops[0], bottoms[0]}) {
            bool valid = true;
            int swap_top = target != tops[0];
            int swap_btm = target != bottoms[0];
            for(int i = 1; i < n; ++i) {
                if(tops[i] != target && bottoms[i] != target) {
                    valid = false;
                    break;
                }
                swap_top += tops[i] != target;
                swap_btm += bottoms[i] != target;
            }
            if(valid) {
                return min(swap_top, swap_btm);
            }
        }
        return -1;
    }
};
