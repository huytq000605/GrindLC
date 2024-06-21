class Solution {
public:
    vector<vector<int>> findRLEArray(vector<vector<int>>& encoded1, vector<vector<int>>& encoded2) {
        int i = 0, j = 0;
        vector<vector<int>> result;
        while(i < encoded1.size() && j < encoded2.size()) {
            auto & e1 = encoded1[i];
            auto & e2 = encoded2[j];
            vector<int> encoded = {e1[0] * e2[0], 0};
            int freq = min(e1[1], e2[1]);
            encoded[1] = freq;
            e1[1] -= freq;
            if(!e1[1]) i++;
            e2[1] -= freq;
            if(!e2[1]) j++;
            if(!result.empty() && result.back()[0] == encoded[0]) 
                result.back()[1] += encoded[1];
            else 
                result.push_back(encoded);
        }
        return result;
    }
};
