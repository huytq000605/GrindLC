class Solution {
public:
    int minFlips(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        
        int flips = 0;
        int ones = 0;
        
        for(int r = 0; r < m; r++) {
            int i = 0, j = n-1;
            while(i < j) {
                if(grid[r][i] != grid[r][j]) {
                    flips++;
                    grid[r][i] = grid[r][j];
                }
                ones += (grid[r][i] == 1) + (grid[r][j] == 1);
                i++;
                j--;
            }
        }
        
        for(int c = 0; c < n; c++) {
            int i = 0, j = m-1;
            while(i < j) if(grid[i++][c] != grid[j--][c]) flips++;
        }
        cout << flips << " " << ones << endl;
        if(m % 2 && n % 2) ones += grid[m/2][n/2];
        if(ones % 4 == 0 || flips >= min(ones % 4, 4 - (ones % 4))) return flips;
        // flips <= ones % 4
        if( (m % 2 && n % 2) && min(ones % 4, 4 - (ones % 4)) == 1) return flips;
        return ones;
    }
};
