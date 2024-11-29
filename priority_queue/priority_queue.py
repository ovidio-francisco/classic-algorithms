import heapq


class PriorityQueue:

    def __init__(self):
        self.heap = []


    def push(self, priority, element):
        if not isinstance(priority, (int, float)):
            raise TypeError("Priority must be a number")
        if element is None:
            raise ValueError("Element can't be None")
        heapq.heappush(self.heap, (priority, element))


    def pop(self):
        if not self.heap:
            raise IndexError("Can't pop from an empty queue")
        return heapq.heappop(self.heap)[1]


    def peek(self):
        if not self.heap:
            return None

        return self.heap[0][1]






