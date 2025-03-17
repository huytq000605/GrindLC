class Solution {
public:
    int numOfUnplacedFruits(vector<int>& fruits, vector<int>& baskets) {
        int n = fruits.size();
        int result = 0;
        for(int f: fruits) {
            bool placed = false;
            for(int i = 0; i < n; ++i) {
                if(baskets[i] >= f) {
                    placed = true;
                    baskets[i] = 0;
                    break;
                }
            }
            if(!placed) ++result;
        }
        return result;
    }
};
