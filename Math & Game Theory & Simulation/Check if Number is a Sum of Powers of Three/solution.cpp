class Solution {
public:
    bool checkPowersOfThree(int n) {
        vector<int> pow3(17);
        pow3[0] = 1;
        for(int i{1}; i < 17; ++i)
            pow3[i] = pow3[i-1] * 3;
        for(int i{16}; i >= 0; --i) 
            if(n >= pow3[i]) n-= pow3[i];
        return n == 0;
    }       
};
