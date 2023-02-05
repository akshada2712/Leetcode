class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [[1]]

        for i in range(rowIndex):
            temp = [0] + res[-1] + [0]
            rows = []

            for j in range(len(res[-1])+1):
                rows.append(temp[j]+temp[j+1])
            res.append(rows)

        return res[rowIndex]
