class Solution {
public:
    vector<int> assignElements(vector<int>& groups, vector<int>& elements) {
        vector<int> result(groups.size(), -1);
        unordered_map<int, int> idxs;
        for(int i = 0; i < elements.size(); ++i) {
            if(idxs.find(elements[i]) == idxs.end()) {
                idxs[elements[i]] = i;
            }
        }
        for(int k = 0; k < groups.size(); ++k) {
            int num = groups[k];
            int res = elements.size();
            for(int i = 1; i * i <= num; ++i) {
                if(num % i == 0) {
                    int j = num / i;
                    int idxi = idxs.find(i) == idxs.end() ? elements.size(): idxs[i];
                    int idxj = idxs.find(j) == idxs.end() ? elements.size(): idxs[j];
                    res = min({res, idxi, idxj});
                }
            }
            if(res != elements.size()) result[k] = res;
        }
        return result;
        
    }
};
