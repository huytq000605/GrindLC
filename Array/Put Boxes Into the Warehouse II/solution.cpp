class Solution {
public:
    int maxBoxesInWarehouse(vector<int>& boxes, vector<int>& warehouse) {
        sort(boxes.rbegin(), boxes.rend());
        int left = 0, right = warehouse.size() - 1;
        int result = 0;
        for(auto box: boxes) {
            if(left > right) break;
            if(box <= warehouse[left]) {
                left++;
                result += 1;
            } else if(box <= warehouse[right]) {
                right--;
                result += 1;
            }
        }
        return result;
    }
};
