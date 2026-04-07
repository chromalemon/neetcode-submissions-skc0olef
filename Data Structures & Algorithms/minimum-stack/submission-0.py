class MinStack:

    def __init__(self):
        self.pointer = -1
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.pointer += 1
        
    def pop(self) -> None:
        self.stack.pop(self.pointer)
        self.pointer -= 1
        
    def top(self) -> int:
        return self.stack[self.pointer]
        
    def getMin(self) -> int:
        smallest = self.stack[0]
        for val in self.stack:
            if val < smallest:
                smallest = val
        return smallest