class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
         
        
        n = len(nums)
        mid = n//2
        
        for i in range(1 , n) :
            if nums[i] < nums[i-1] :
                mid = i-1
                break
        #print(mid)
        i = 0
        j = n-1
        
        if target == nums[mid] :
            return mid 
        elif target < nums[mid] and target >= nums[0] :
            j = mid-1
        else:
            i = mid+1
        # print(mid)
        # print(i , j)
        while(i<= j) :
            mid = (i+j)//2
            
            if target == nums[mid] :
                return mid
            elif target < nums[mid] :
                j = mid-1 
            else:
                i = mid+1
        
        return -1
    
        