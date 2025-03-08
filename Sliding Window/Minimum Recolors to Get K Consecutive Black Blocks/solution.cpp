class Solution {
public:
    int minimumRecolors(string blocks, int k) {
        int result = k;
        for(int i{}, black{}; i < blocks.size(); ++i) {
            if(i - k >= 0) {
                black -= blocks[i-k] == 'B';
            }
            black += blocks[i] == 'B';
            result = min(result, k - black);
        }
        return result;
    }
};
