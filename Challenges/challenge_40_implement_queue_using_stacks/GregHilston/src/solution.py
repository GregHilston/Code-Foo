class GrehgStack:
    def __init__(self):
        self.data = []

    def push(self, element: any):
        self.data.append(element)

    def peek(self) -> any:
        if len(self.data) > 0:
            return self.data[-1]
        else:
            return None

    def pop(self) -> any:
        return self.data.pop()

    def empty(self) -> any:
        return len(self.data) == 0

class GrehgQueue:
    def __init__(self):
        self.grehgStack = GrehgStack()

    def push(self, element: any):
        temp = []

        # Remove all the data from the stack
        while self.grehgStack.peek():
            temp.append(self.grehgStack.pop())

        # Add our new data
        self.grehgStack.push(element)

        # Re Add our data from the stack
        while len(temp) != 0:
            self.grehgStack.push(temp.pop())

    def peek(self) -> any:
        return self.grehgStack.peek()

    def pop(self) -> any:
        temp = []

        # Remove all the data from the stack
        while self.grehgStack.peek():
            temp.append(self.grehgStack.pop())

        # Add our new data
        popped = temp.pop(0)

        # Re Add our data from the stack
        while len(temp) != 0:
            self.grehgStack.push(temp.pop())

        return popped

    def empty(self) -> any:
        return self.grehgStack.empty()