class Solution {
public:
    string fractionAddition(string expression) {
        int sign = 1;
        int numerator = 0;
        int denominator = 1;
        for(int i = 0; i < expression.size(); i++) {
            if(expression[i] == '-') sign = -1;
            else if(expression[i] == '+') sign = 1;
            else if(expression[i] == '/') {
                int num = sign * (i-2 >= 0 && expression[i-2] == '1' ? 10: expression[i-1] - '0');
                int deno = i+2 < expression.size() && expression[i+2] == '0' ? 10: expression[i+1] - '0';
                int gcd = std::lcm(denominator, deno);
                num *= gcd / deno;
                numerator *= gcd / denominator;
                denominator = gcd;
                numerator += num;
            }
        }
        if(!numerator) return "0/1";
        for(int d = 9; d >= 2; --d) {
            if(numerator % d == 0 && denominator %d == 0) {
                numerator /= d;
                denominator /= d;
            }
        } 
        return to_string(numerator) + "/" + to_string(denominator);
    }
};
