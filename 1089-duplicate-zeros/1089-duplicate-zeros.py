class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        ans=[]
        i=0
        while len(ans)<len(arr):
            if arr[i]!=0:
                ans.append(arr[i])
            else:
                ans.append(0)
                if len(ans)<len(arr):
                    ans.append(0)
            i+=1
        for i in range(len(ans)):
            arr[i]=ans[i]
        return arr


            
            