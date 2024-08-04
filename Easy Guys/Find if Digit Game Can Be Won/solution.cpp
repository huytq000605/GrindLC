class Solution {
public:
    bool canAliceWin(vector<int>& nums) {
        int one = 0, two = 0;
        for(auto num: nums) {
            if(num >= 10) {
                two += num;
            } else {
                one += num;
            }
        }
        return one != two;
    }
};
