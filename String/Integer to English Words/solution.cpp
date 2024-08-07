class Solution {
public:
    string numberToWords(int num) {
        if(!num) return "Zero";
        auto below_1000 = [](int num, auto ref) -> string {
            if(!num) return "";
            if(num < 20) return below_20[num];
            if(num < 100) return tens[num/10] + (num % 10 ? " " + below_20[num % 10] : "");
            return below_20[num/100] + HUNDRED + (num%100 ? " " + ref(num%100, ref) : "");
        };
        string result;
        int i = 0;
        while(num) {
            if(num % 1000) {
                result = below_1000(num % 1000, below_1000) + " " + thousands[i] + result; 
            }
            num /= 1000;
            i++;
        }
        return result.substr(0, result.size() - 1);
    }
private:
    static constexpr array<string, 21> below_20{"", "One", "Two", "Three", "Four","Five","Six","Seven","Eight","Nine","Ten", "Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"};
    static constexpr array<string, 10> tens{"", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"};
    static constexpr array<string, 4> thousands{"","Thousand ","Million ","Billion "};
    static constexpr string HUNDRED = " Hundred";
};
