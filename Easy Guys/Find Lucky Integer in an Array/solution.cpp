class Solution {
public:
    int findLucky(vector<int>& arr) {
        int mx = *max_element(arr.begin(), arr.end());
        vector<int> freq(mx+1);
        for(auto num: arr) freq[num]++;
        int result = -1;
        for(int num = 1; num <= mx; ++num) {
            if(freq[num] == num) result = num;
        }
        return result;
    }
};
