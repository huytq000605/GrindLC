class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        sort(people.begin(), people.end());
        int boats = 0;
        auto i = people.begin(), j = people.end() - 1;
        while(i <= j) {
            boats += 1;
            if(i < j && *j + *i <= limit) {
                i += 1;
            }
            j -= 1;
        }
        return boats;
    }
};
