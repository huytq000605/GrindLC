class Solution {
public:
    int bestClosingTime(string customers) {  
        int result = -1;
        int penalty = count(begin(customers), end(customers), 'Y');
        int min_penalty = penalty;
        for(int i = 0; i < customers.size(); ++i) {
            char c = customers[i];
            if(c == 'Y') {
                penalty--;
            } else {
                penalty++;
            }
            if(penalty < min_penalty) {
                min_penalty = penalty;
                result = i;
            }
        }
        return result+1;
    }
};
