class Solution {
public:
    string kthDistinct(vector<string>& arr, int k) {
        map<string, int> counter;
        for(auto c: arr) counter[c]++;
        for(auto c: arr) {
            if(counter[c] == 1) k--;
            if(!k) return c;
        }
        return "";
    }
};
