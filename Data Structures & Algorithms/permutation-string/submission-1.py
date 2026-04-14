class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        import copy
        n1, n2 = len(s1), len(s2)
        mp1 = defaultdict(int)
        orig = []
        for char in s1:
            mp1[char] += 1
            orig.append(char)
        mp2 = copy.copy(mp1)
        i, j = 0, 0
        while i < n2:
            if s2[i] in mp1:
                j = i
                sub = []
                while j < n2 and mp2[s2[j]] > 0:
                    sub.append(s2[j])
                    mp2[s2[j]] -= 1
                    j += 1
                j -= 1
                if sorted(sub) == sorted(orig) and len(sub) == len(orig):
                    return True
                if j+1 < n2 and s2[j+1] not in mp1:
                    i = j

            i += 1
            mp2 = copy.copy(mp1)
        
        return False