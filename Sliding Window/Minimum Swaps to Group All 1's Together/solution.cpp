class Solution {
public:
    int minSwaps(vector<int>& data) {
        int k = 0;
        for(int num: data) if(num) ++k;
        int mx = 0;
        for(int i = 0, ones = 0; i < data.size(); ++i) {
            if(i - k >= 0) {
                ones -= data[i-k] == 1;
            }
            ones += data[i];
            mx = max(mx, ones);
        }
        return k - mx;
    }
};
