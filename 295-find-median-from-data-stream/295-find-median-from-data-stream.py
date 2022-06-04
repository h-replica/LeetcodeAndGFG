import heapq as h
class MedianFinder:

    def __init__(self):
        self.rightminheap = []
        self.leftmaxheap = []
        self.n = 0
        self.l = 0
        self.r = 0
    
    def balanceHeaps(self) :
        l = len(self.leftmaxheap)
        r = len(self.rightminheap)
        if l < 1 or r < 1 :
            return
        while(self.rightminheap[0] < self.leftmaxheap[0]) :
            toleft = h.heappop(self.rightminheap)
            toright = h._heappop_max(self.leftmaxheap)
            
            h.heappush(self.rightminheap , toright)
            self.leftmaxheap.append(toleft)
            h._siftdown_max(self.leftmaxheap , 0 , len(self.leftmaxheap)-1)
            
        l = len(self.leftmaxheap)
        r = len(self.rightminheap)
        
        while(l - r > 1) :
            toright = h._heappop_max(self.leftmaxheap)
            h.heappush(self.rightminheap , toright)
            l-=1
            r+=1
        
        while(r-l > 1) :
            toleft = h.heappop(self.rightminheap)
            self.leftmaxheap.append(toleft)
            h._siftdown_max(self.leftmaxheap , 0 , len(self.leftmaxheap)-1)
            
            r-=1
            l+=1
        
        self.l = l
        self.r = r
            
            
            

    def addNum(self, num: int) -> None:
        self.n+=1
        if self.l > self.r :
            h.heappush(self.rightminheap , num)
            self.r+=1
            self.balanceHeaps()
        else:
            self.leftmaxheap.append(num)
            h._siftdown_max(self.leftmaxheap , 0 , self.l)
            self.l+=1
            self.balanceHeaps()
        # print(num)
        # print(self.leftmaxheap)
        # print(self.rightminheap)

    def findMedian(self) -> float:
        # print(self.leftmaxheap)
        # print(self.rightminheap)
        # return 1
        if self.n < 2 :
            if self.l > 0 :
                return self.leftmaxheap[0]
            elif self.r > 0 :
                return self.rightminheap[0]
            else :
                return None
        leftmax = self.leftmaxheap[0]
        rightmin = self.rightminheap[0]
        
        if self.n % 2 == 0 :
            return (leftmax + rightmin)/2
        else :
            if self.l > self.r  :
                return leftmax
            return rightmin
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()