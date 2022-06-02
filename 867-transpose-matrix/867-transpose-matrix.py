class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n , m = len(matrix) , len(matrix[0])
        ans = []
        for i in range(m) :
            add = []
            for j in range(n) :
                add.append(matrix[j][i])
            ans.append(add)
        
        return ans
        