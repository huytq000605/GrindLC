class Solution {
public:
    int minSwaps(string s) {
        int misplaced = 0;
        int st = 0;
        for(auto c: s) {
            if(c == '[') ++st;
            else --st;
            if(st < 0) {
                ++misplaced;
                st = 0;
            }
        }
        misplaced += st;
        // 1 swap can fix 2 pairs = 4 positions
        return (misplaced + 3) / 4;
    }
};
