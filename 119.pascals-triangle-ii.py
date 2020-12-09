class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        return [1] if rowIndex == 0 else (lambda row: [1 if i == 0 or i == rowIndex else row[i - 1] + row[i] for i in range(rowIndex + 1)])(self.getRow(rowIndex - 1))
