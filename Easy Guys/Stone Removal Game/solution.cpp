class Solution {
public:
    bool canAliceWin(int n) {
        bool alice{true};
        int k{10};
        while(n >= 0) {
            n -= k--;
            alice = !alice;
            
        }
        return alice;
    }
};
