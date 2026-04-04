class Solution {
public:
    string decodeCiphertext(string encodedText, int rows) {
        int n = encodedText.size();
        string result;
        int cols = n / rows;
        for(int col = 0; col < n; ++col) {
            for(int r = 0, c = col; r < rows && c < cols; ++r, ++c) {
                result += encodedText[r * cols + c];
            }
        }
        while(!result.empty() && result.back() == ' ') result.pop_back();
        return result;
    }
};
