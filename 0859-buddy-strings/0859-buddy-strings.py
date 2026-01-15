class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if s==goal:
            s1=list(Counter(s).values())
            return max(s1)>=2
        if Counter(s)==Counter(goal):
            b=[]
            for i in range(len(s)):
                if s[i]!=goal[i]:
                    b.append(i)
            return len(b)==2
        return False


        