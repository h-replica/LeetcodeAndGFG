class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        """
            Approach :- for every element in strs we can either include it in our answer or we dont 
            
            it is almost same as 0/1 knapsack 
            for memorisation :- see what's keep on changing , ( think every variable in as if they are column of a 
            SQL table then what columns will contribute in making composite primary key - this may not work 
            every where but it will help the thought process)
        
        """
        onesandzeros = []
        for i in strs :
            onesandzeros.append([i.count("1") , i.count("0")])
        print(onesandzeros)
        ans = 0
        @cache
        def formsubsets( m , n , i , j , included , at) :
            nonlocal ans
            if i > n or j > m :
                ans = max(ans , included-1)
                return
            
            if at == len(strs) :
                ans = max(ans , included)
                return 
            
            formsubsets( m , n , i , j , included , at+1)
            formsubsets( m , n , i + onesandzeros[at][0] , j + onesandzeros[at][1] , included+1 , at+1)
        formsubsets( m , n , 0 , 0 , 0 , 0)
        return ans
            
            