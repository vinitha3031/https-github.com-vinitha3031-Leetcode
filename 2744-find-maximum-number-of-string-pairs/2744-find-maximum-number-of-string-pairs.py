class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        cnt=0
        for i in range(len(words)):
            a=cnt
            for j in words[i+1:]:
                if Counter(words[i])==Counter(j):
                    cnt+=1
                    break
        return cnt