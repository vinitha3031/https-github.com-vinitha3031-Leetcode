class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        a=0
        b=0
        for i in bills:
            if i==20:
                if a>=1 and b>=1:
                    b-=1
                    a-=1
                elif b==0 and a>=3:
                    a-=3
                else:
                    return False
            elif i==10:
                b+=1
                if a:
                    a-=1
                else:
                    return False
            else:
                a+=1
        return True
            

                


