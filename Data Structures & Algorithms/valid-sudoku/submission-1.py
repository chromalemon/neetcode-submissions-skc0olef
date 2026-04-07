class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seen = defaultdict(int)
            for x in range(9):
                if board[i][x] in seen and board[i][x].isdigit():
                    return False
                else:
                    seen[board[i][x]] += 1
        for j in range(9):
            seen = defaultdict(int)
            for y in range(9):
                if board[y][j] in seen and board[y][j].isdigit():
                    return False
                else:
                    seen[board[y][j]] += 1
        for a in range(3):
            for b in range(3):
                seen = defaultdict(int)
                for c in range(3):
                    for d in range(3):
                        curr = board[c+3*a][d+3*b] 
                        if curr in seen and curr.isdigit():
                            return False
                        else:
                            seen[curr] += 1
        return True