class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n2 < n1:
            return False
        mp1 = {chr(i): 0 for i in range(ord("a"), ord("z")+1)}
        mp2 = {chr(i): 0 for i in range(ord("a"), ord("z")+1)}
        for char in s1:
            mp1[char] += 1
        i = 0
        for char in s2[0:n1]:
            mp2[char] += 1
        if mp1 == mp2:
            return True
        j = n1
        while j < n2:
            mp2[s2[i]] -= 1
            mp2[s2[j]] += 1
            if mp1 == mp2:
                return True
            i += 1
            j += 1
        return False
        