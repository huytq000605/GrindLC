class Spreadsheet {
vector<vector<int>> sheet;
public:
    Spreadsheet(int rows) {
        sheet.resize(26);
        for(int i = 0; i < 26; ++i) {
            sheet[i].resize(rows);
        }
    }
    
    void setCell(string cell, int value) {
        int column = cell[0] - 'A';
        int row = stoi(cell.substr(1)) - 1;
        sheet[column][row] = value;
    }
    
    void resetCell(string cell) {
        int column = cell[0] - 'A';
        int row = stoi(cell.substr(1)) - 1;
        sheet[column][row] = 0;
    }
    
    int getValue(string formula) {
        array<string, 2> vs;
        for(int i = 1, j = 0; i < formula.size(); ++i) {
            if(formula[i] == '+') {
                ++j;
                continue;
            }
            vs[j] += formula[i];
        }
        int left = value(vs[0]), right = value(vs[1]);
        return left + right;
    }
    
    int value(string& v) {
        if(isalpha(v[0])) {
            int column = v[0] - 'A';
            int row = stoi(v.substr(1)) - 1;
            return sheet[column][row];
        }
        return stoi(v);
    }
};

/**
 * Your Spreadsheet object will be instantiated and called as such:
 * Spreadsheet* obj = new Spreadsheet(rows);
 * obj->setCell(cell,value);
 * obj->resetCell(cell);
 * int param_3 = obj->getValue(formula);
 */
