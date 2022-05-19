import collections as col
class Solution:
    def twoSum(self, nums: List[int],x: int) -> List[int]:
        a = col.defaultdict(list)
        for i in range(len(nums)) :
            a[nums[i]].append(i)
        
        for i in nums :
            if x-i in a  :
                if (x-i == i and len(a[i]) > 1 ) or x-i != i:
                    return [a[i][0] , a[x-i][0] if x-i != i else a[x-i][1]]
            
            
        