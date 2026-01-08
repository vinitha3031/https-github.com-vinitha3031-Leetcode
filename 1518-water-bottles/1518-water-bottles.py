class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans=numBottles 
        a=numBottles 
        while a>=numExchange:
            b=a//numExchange%a
            ans+=b
            a=b+(a%numExchange)
        return ans

        