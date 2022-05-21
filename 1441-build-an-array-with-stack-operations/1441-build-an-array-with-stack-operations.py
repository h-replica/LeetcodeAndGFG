class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        s = set(target)
        maxm = max(target)
        for i in range(1 , maxm+1) :
            if i in s :
                ans.append("Push")
            else:
                ans.append("Push")
                ans.append("Pop")
        return ans