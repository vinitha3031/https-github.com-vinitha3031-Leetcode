class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        a=set(Counter(s).values())
        return len(a)==1
        