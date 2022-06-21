class Solution:
    def furthestBuilding(self, h: List[int], bricks: int, ladders: int) -> int:
        heap=[]
        heapify(heap)
        for i in range(len(h)-1):
            d=h[i+1]-h[i]
            if d>0:
                heappush(heap,d)
                if len(heap)>ladders:
                    bricks-=heappop(heap)
                    if bricks<0:
                        return i
        return len(h)-1
		