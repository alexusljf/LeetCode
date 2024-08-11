class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1/x
            n = -n
        
        def helper(x,n):
            if n == 0: return 1
            half = helper(x,n//2)
            if n % 2 == 0: # if n even -> x^n = x^n/2 * x^n/2
                return half * half 
            else:  # else n odd -> x^n = x^n/2 * x^n/2 * x
                return x * half  * half 
        return helper(x,n)
        