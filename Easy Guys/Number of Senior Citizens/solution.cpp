class Solution {
public:
    int countSeniors(vector<string>& details) {
        int result = 0;
        for(auto detail: details) {
            auto age_str = detail.substr(11, 2);
            auto age = (age_str[0] - '0') * 10 + (age_str[1] - '0');
            if(age > 60) result++;
        }
        return result;
    }
};
