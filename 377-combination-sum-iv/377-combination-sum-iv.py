class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        if n == 0 :
            return 0 
        dp = {}
        dp[0] = 1
        
        def ans(x):
            if x == 0 :
                return 1 
            if x in dp :
                return dp[x]
            total = 0
            for num in nums :
                if num > x :
                    continue
                elif num == x :
                    total+=1
                else :
                    total += ans(x - num)
            dp[x] = total
            return total
        
        return ans(target)
                
        