# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]

# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.




class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.rec(board, i,j, word):
                    return True
            
        return False
    
    def rec(self,board,i,j,word):
        if (len(word) == 0): # all the characters are checked
            return True
        
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or board[i][j] != word[0]:
            return False
        
        t = board[i][j] # first character is found, check the remaining part
        
        board[i][j] = "#" # avoid visit agian
        # check whether can find "word" along one direction
        ans = self.rec(board,i+1,j,word[1:]) or self.rec(board,i-1,j,word[1:]) or self.rec(board,i,j+1,word[1:]) or self.rec(board,i,j-1,word[1:])
        
        board[i][j] = t
        
        return ans