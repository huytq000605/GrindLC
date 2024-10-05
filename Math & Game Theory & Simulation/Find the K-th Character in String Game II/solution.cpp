class Solution {
public:
    char kthCharacter(long long k, vector<int>& operations) {
        long long length = 1;
        int i = -1;
        while(length < k) {
            length *= 2;
            ++i;
        }
        int increased = 0;
        while(length > 1) {
            if(k > length / 2) {
                increased += operations[i];
                k -= length / 2;
            }
            --i;
            length /= 2;
        }
        return increased % 26 + 'a';
    }
};
