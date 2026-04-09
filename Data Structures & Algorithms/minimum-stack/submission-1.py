class MinStack:

    def __init__(self):
        self.stack = []
        self.pointer = -1
        self.minimum = float("inf")
        self.min_pointer = -1

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.pointer += 1
        if val < self.minimum:
            self.minimum = val
            self.min_pointer = self.pointer


    def pop(self) -> None:
        self.stack.pop()
        minimum = float("inf")
        min_pointer = -1
        for index, num in enumerate(self.stack):
            if num < minimum:
                minimum = num
                min_pointer = index
        self.minimum = minimum
        self.min_pointer = min_pointer
        self.pointer -= 1

    def top(self) -> int:
        return self.stack[self.pointer]

    def getMin(self) -> int:
        return self.stack[self.min_pointer]
