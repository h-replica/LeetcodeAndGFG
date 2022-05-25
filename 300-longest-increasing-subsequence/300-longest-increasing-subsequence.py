class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        def findrightpos(arr , l , r , key) :
            
            while(r - l > 1) :
                mid = l + (r - l)//2
                if arr[mid] >= key :
                    r = mid
                else:
                    l = mid
            return r
    
        if len(nums) ==1 :
            return 1
        
        listcontainer = [0 for i in range(n)]
        
        listcontainer[0] = nums[0]
        lenlis = 1
        
        for i in range(1 , n) :
            if nums[i] < listcontainer[0] :
                listcontainer[0] = nums[i]
            elif nums[i] > listcontainer[lenlis-1] :
                listcontainer[lenlis] = nums[i]
                lenlis+=1
            else:
                listcontainer[findrightpos(listcontainer , -1 , lenlis-1 , nums[i])] = nums[i]
        return lenlis
        
        