class Solution {
public:
    char kthCharacter(int k) {
        int i = -1;
        long long length = 1;
        while(length < k) {
            length *= 2;
            ++i;
        }
        int increased = 0;
        while(length > 1) {
            if(k > length / 2) {
                k -= length / 2;
                ++increased;
            }
            length /= 2;
            --i;
        }
        return increased % 26 + 'a';
    }
};
