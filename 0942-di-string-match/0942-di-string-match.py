class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        a=[i for i in range(len(s)+1)]
        ans=[]
        for i in s:
            if i=="I":
                ans.append(a[0])
                a.remove(a[0])
            else:
                ans.append(a[-1])
                a.pop()
        if a:
            ans.append(a[-1])
        return ans