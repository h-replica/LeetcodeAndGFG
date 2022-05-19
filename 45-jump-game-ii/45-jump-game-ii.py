class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        least = [i for i in range(n)]
        farthest = 0
        for i in range(n) :
            newf = i + nums[i]
            if newf > n-1 :
                newf = n-1
            for j in range(i+1 , newf+1) :
                least[j] = min(least[j] , least[i]+1)
            # if i <= farthest :
            #     newf = i + nums[i]
            #     farthest = max(farthest , newf)
        return least[n-1]
                
        
        