class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        n = len(nums)
        i = 0 
        j = n-1
        
        flag = 0
        while(i<=j) :
            mid = (i+j)//2
            
            if target == nums[mid] :
                flag = 1
                break
            elif target < nums[mid] :
                j = mid-1
            else :
                i = mid+1
        
        if flag == 0 :
            return [-1 , -1]
            
        return [bisect_left(nums , target) , bisect_right(nums , target)-1]