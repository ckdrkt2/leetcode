class Solution:
    def guessNumber(self, n: int) -> int:
        l=1
        r=n
        while l<=r:
            m=l+(r-l)//2
            if(guess(m)==-1):
                r=m
            elif(guess(m)==1):
                l=m+1
            else:
                return m