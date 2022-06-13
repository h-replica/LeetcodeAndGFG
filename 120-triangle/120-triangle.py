class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        @cache
        def soln(index , level) :
            if level == n :
                return 0
            sameidx = soln(index , level+1)
            nextidx = soln(index+1 , level+1)
            
            return min(sameidx , nextidx) + triangle[level][index]
        
        return soln(0 , 0)
            