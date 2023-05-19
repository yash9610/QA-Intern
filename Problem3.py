from queue import Queue

class Stack:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, element):
        self.queue2.put(element)

        # Move all elements from queue1 to queue2
        while not self.queue1.empty():
            self.queue2.put(self.queue1.get())

        # Swap the names of queue1 and queue2
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self):
        if self.queue1.empty():
            raise IndexError("Stack is empty. Cannot perform pop operation.")

        return self.queue1.get()

    def top(self):
        if self.queue1.empty():
            raise IndexError("Stack is empty")

        return self.queue1.queue[0]

# Example:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.top())

print(stack.pop())

print(stack.top()) 




