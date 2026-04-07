class Solution:
    def isValid(self, s: str) -> bool:
        c = {"(":")", "[":"]","{":"}"}
        a = [""] * len(s)
        top = -1
        for S in s:
            if S in c:
                top += 1
                a[top] = c[S]
            else:
                if S != a[top]:
                    return False
                top -= 1
        if top == -1:
            return True
        return False

                

        