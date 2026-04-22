class Solution {
public:
    vector<string> twoEditWords(vector<string>& queries, vector<string>& dictionary) {
        vector<string> result;
        for(auto &q: queries) {
            bool valid = false;
            for(auto &w: dictionary) {
                int diff = 0;
                for(int i = 0; i < w.size(); ++i) diff += w[i] != q[i];
                if(diff <= 2) {
                    valid = true;
                    break;
                }
            }
            if(valid) result.push_back(q);
        }
        return result;
    }
};
