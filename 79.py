class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        if not board:
            return False
        if not word:
            return True 

        def dfs(i, j, index): 
            if index == len(word):
                return True 
            if i < 0 or i == len(board) or j < 0 or j == len(board[0]) or board[i][j] != word[index]:
                return False
            # mark as visited 
            board[i][j] = "*"
            exists = dfs(i + 1, j, index + 1) or dfs(i - 1, j, index + 1) or dfs(i, j + 1, index + 1) or dfs(i, j - 1, index + 1)
            board[i][j] = word[index] 
            return exists

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False
        