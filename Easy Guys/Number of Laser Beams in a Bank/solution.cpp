class Solution {
public:
    int numberOfBeams(vector<string>& bank) {
        int result = 0;
        int prev_row = 0;
        for(auto &r: bank) {
            int devices = 0;
            for(auto c: r) {
                if(c == '1') ++devices;
            }
            if(devices) {
                result += devices * prev_row;
                prev_row = devices;
            }
        }
        return result;
    }
};
