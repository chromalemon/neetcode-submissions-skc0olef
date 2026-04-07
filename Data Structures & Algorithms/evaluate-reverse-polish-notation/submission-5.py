class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #ord between 48 and 57 inclusive is digits.
        from math import floor
        op = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: x / y
            }
        stack = []
        top = -1
        for c in tokens:
            if c not in op:
                stack.append(int(c))
                top += 1
                print(stack)
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(math.trunc(op[c](num2, num1)))
                print(stack)
        return math.trunc(stack[0])