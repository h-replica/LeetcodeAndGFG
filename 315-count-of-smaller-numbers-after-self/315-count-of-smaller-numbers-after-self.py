class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        arr = sorted(nums)
        ans = []
        
        for x in nums :
            i = bisect_left(arr , x)
            ans.append(i)
            del arr[i]
        return ans