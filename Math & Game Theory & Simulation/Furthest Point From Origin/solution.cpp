class Solution {
public:
    int furthestDistanceFromOrigin(string moves) {
        int all_left = 0;
        int all_right = 0;
        for(auto c: moves) {
            if(c == 'L') {
                all_left++;
                all_right--;
            }
            else if(c == 'R') {
                all_left--;
                all_right++;
            } 
            else {
                all_left++;
                all_right++;
            }
        }
        return max(all_left, all_right);
    }
};
