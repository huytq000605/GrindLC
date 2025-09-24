class Solution {
public:
    string fractionToDecimal(int64_t n, int64_t d) {
        if(!n) return "0";
        unordered_map<int, int> seen;
        string result;
        int negative = (n<0) ^ (d<0);
        if(negative) result += '-';
        n = abs(n);
        d = abs(d);
        result += to_string(n / d);
        n = n % d * 10;
        if(n) result += '.';
        while(n) {
            if(seen.find(n) != seen.end()) {
                result.insert(seen[n], 1, '(');
                result += ')';
                return result;
            }
            seen[n] = result.size();
            result += to_string(n / d);
            n = n % d * 10;
        }
        return result;
    }
};
