class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        stack1 = []
        stack2 = []
        
        for i in s :
            if i == "#" and len(stack1) != 0 :
                stack1.pop()
            elif i != "#" :
                stack1.append(i)
        
        for i in t :
            if i == "#" and len(stack2) != 0 :
                stack2.pop()
            elif i != "#" :
                stack2.append(i)
                
        return stack1 == stack2
                
        