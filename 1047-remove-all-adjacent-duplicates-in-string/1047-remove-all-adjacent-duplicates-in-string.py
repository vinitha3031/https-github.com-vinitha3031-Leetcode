class Solution:
    def removeDuplicates(self, s: str) -> str:
        a=[]
        for i in s:
            if a and a[-1]==i:
                a.pop()
            else:
                a.append(i)
        print(a)
        return "".join(a)
            
                
                

