class Solution {
public:
    vector<int> arraysIntersection(vector<int>& arr1, vector<int>& arr2, vector<int>& arr3) {
        int i{0}, j{0}, k{0};
        vector<int> result{};
        while(i < arr1.size() && j < arr2.size() && k < arr3.size()) {
            if(arr1[i] == arr2[j] && arr2[j] == arr3[k]) {
                result.emplace_back(arr1[i]);
                ++i;
                ++j;
                ++k;
            } else {
                int mn = min({arr1[i], arr2[j], arr3[k]});
                if(arr1[i] == mn) ++i;
                if(arr2[j] == mn) ++j;
                if(arr3[k] == mn) ++k;
            }
        }
        return result;
    }
};
