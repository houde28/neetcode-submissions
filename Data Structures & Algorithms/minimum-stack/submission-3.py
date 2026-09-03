class MinStack:

    def __init__(self):
        self.stack=[]
        self.extraStack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.extraStack:
            self.extraStack.append(val)
        elif self.extraStack[-1] > val:
            self.extraStack.append(val)
        else:
            self.extraStack.append(self.extraStack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.extraStack.pop()


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.extraStack[-1]
        
        