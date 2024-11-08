class Solution {
public:
    bool isBalanced(string num) {
        int odd{0}, even{0};
        for(int i{0}; i < num.size(); ++i) {
            if(i & 1) odd += num[i] - '0';
            else even += num[i] - '0';
        }
        return even == odd;
    }
};
