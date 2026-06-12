class Solution {
public:
    string addBinary(string a, string b) {
        string result;
        int i =  a.size() - 1, j = b.size() - 1;
        int rmb = 0;
        while(i >= 0 || j >= 0 || rmb) {
            int v = (i >= 0 ? (a[i] - '0'): 0) + (j >= 0 ? (b[j] - '0'): 0) + rmb;
            if(v >= 2) rmb = 1;
            else rmb = 0;
            result += static_cast<char>((v & 1) + '0'); 
            --i;
            --j;
        }
        reverse(result.begin(), result.end());
        return result;
    }
};
