class stack:
    def __init__(self):
        self.container = []

    def push(self,val):
        self.container.append(val)
        print(f"Pushed: {val}")

    def pop(self):
        popped = self.container.pop()
        print(f"Popped: {popped}")
        return popped

    def peek(self): #latest of the container
        peek = self.container[-1]
        print(f"Peeked: {peek}")
        return peek

#lets create a stack object
s = stack()
s.push("https://idrw.org/")
s.push("https://idrw.org/category/india/")
s.push("https://idrw.org/category/news-beat/")
s.push("https://idrw.org/category/afi/")
print("Current stack:", s.container)
s.peek()
s.pop()
print("Final stack:", s.container)