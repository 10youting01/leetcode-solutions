class Solution {
private:
    vector<vector<bool>> visited;
    string word;
    int row;
    int col;
    int word_len;
public:
    bool exist(vector<vector<char>>& board, string word) {
        row = board.size();
        col = board[0].size();
        word_len = word.size();
        this->word = word;
        visited.assign(row, vector<bool>(col, false));
        for(int i = 0; i < row; i++){
            for(int j = 0; j < col; j++){
                if(board[i][j] == word[0]){
                    if(dfs(board, 0, i, j)) return true;
                }
            }
        }
        return false;
    }

    bool dfs(vector<vector<char>>& board, int char_idx, int i, int j){
        if(char_idx == word_len) return true;
        if(i < 0 || i >= row || j < 0 || j >= col) return false;
        if(visited[i][j]) return false;
        if(board[i][j] != word[char_idx]) return false;
        
        visited[i][j] = true;

        bool up = dfs(board, char_idx+1, i-1, j);
        bool down = dfs(board, char_idx+1, i+1, j);
        bool left = dfs(board, char_idx+1, i, j-1);
        bool right = dfs(board, char_idx+1, i, j+1);

        visited[i][j] = false;

        return up || down || left || right;
    }
};