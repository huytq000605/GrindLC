class Solution {
public:
    int countStudents(vector<int>& students, vector<int>& sandwiches) {
        int wants[2];
        for(auto & s: students) {
            wants[s] += 1;
        }
        int result = students.size();
        size_t k = 0;
        while(k < sandwiches.size() && wants[sandwiches[k]] > 0) {
            wants[sandwiches[k]]--;
            k += 1;
            result -= 1;
        }
        return result;
    }
};
