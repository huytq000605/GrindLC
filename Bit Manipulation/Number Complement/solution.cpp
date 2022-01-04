class Solution {
public:
    int findComplement(int num) {
        string bin = "";
        while(num > 0) {
            bin = to_string(num % 2) + bin;
            num /= 2;
        }
        int result = 0;
        for(int i = 0; i < bin.length(); i++) {
            if(bin[i] == '0')
                result += (1 << (bin.length() - i - 1));
        }
        return result;
    }
};