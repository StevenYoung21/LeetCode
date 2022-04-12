from ctypes import sizeof


class Solution:
    def isValidSudoku(self, board) -> bool:

        temp = []

        arr1 = [ []  for _ in range(9) ]

        arr2 = [ []  for _ in range(9)]

        arr3 = [ [] for _ in range(3) for _ in range(3) ]

        for i in range(9):
            for j in range(9):
                ch = board[i][j]
                if ch == "." : continue
                if ch in arr1[i] or ch in arr2[j] or ch in arr3[i//3*3+j//3]:
                    return False
                arr1[i].append(ch)
                arr2[j].append(ch)
                arr3[i//3*3+j//3].append(ch)



        return True

board = [
 ["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]



s1 = Solution()
res = s1.isValidSudoku(board)

print(res)