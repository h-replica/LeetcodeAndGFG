from typing import List
import heapq

class Solution:
    def kthLargest(self, N : int, k : int, Arr : List[int]) -> int:
        # code here
        h = []
        for i in range(N) :
            summ = Arr[i]
            h.append(summ)
            heapq._siftdown_max(h , 0 , len(h)-1)
            for j in range(i+1 , N) :
                summ += Arr[j]
                h.append(summ)
                heapq._siftdown_max(h , 0 , len(h)-1)
        for i in range(k) :
            if i == k-1 :
                return heapq._heappop_max(h)
            heapq._heappop_max(h)
                
                


#{ 
#  Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N = int(input())
        
        
        K = int(input())
        
        
        Arr=IntArray().Input(N)
        
        obj = Solution()
        res = obj.kthLargest(N, K, Arr)
        
        print(res)
        

# } Driver Code Ends