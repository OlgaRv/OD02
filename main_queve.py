# формирование очереди
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


queue = Queue()

print(queue.is_empty())

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.is_empty())
print(queue.size())
print(queue.dequeue())
print(queue.size())