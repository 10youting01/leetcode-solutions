class Solution {
private:
    int m;
    int n;
    vector<vector<int>> visited;
public:
    int numIslands(vector<vector<char>>& grid) {
        m = grid.size();
        n = grid[0].size();
        visited.assign(m, vector<int>(n, 0)); 
        int island = 0;

        for (int r = 0; r < m; r++){
            for (int c = 0; c < n; c++){
                if (grid[r][c] == '1' && visited[r][c] == 0){
                    island ++;
                }
                checkAround(grid, r, c);
            }
        }   
        return island;     
    }

    void checkAround(vector<vector<char>>& grid, int row, int col){
        if (row < 0 || col < 0 || row >= m || col >= n) return;
        if (visited[row][col] == 1) return;
        if (grid[row][col] == '0'){
            visited[row][col] = 1;
            return;
        }

        visited[row][col] = 1;
        
        checkAround(grid, row-1, col); // up
        checkAround(grid, row+1, col); // down
        checkAround(grid, row, col-1); // left
        checkAround(grid, row, col+1); // right

        return;
    }
};