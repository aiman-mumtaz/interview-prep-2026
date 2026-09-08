class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_set<char> row[9], col[9], box[9];
        for(int i=0;i<9;i++){
            for(int j=0;j<9;j++){
                char x = board[i][j];
                if(x == '.'){
                    continue;
                }
                int boxIndex = (i/3)*3 + (j/3);
                if(row[i].count(x) || col[j].count(x) || box[boxIndex].count(x)){
                    return false;
                }
                row[i].insert(x);
                col[j].insert(x);
                box[boxIndex].insert(x);
            }
        }
        return true;
    }
};