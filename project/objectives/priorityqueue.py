class PriorityQueue:
    def __init__(self, compare=lambda x : x):
        self.priority_queue = [] # Empty list
        self.compare = compare # Function used to compare

    def push(self, value):
        self.priority_queue.append(value)
        self.priority_queue.sort(key=self.compare)

    def pop(self):
        return self.priority_queue.pop(0) if not self.is_empty() else None

    def is_empty(self):
        return len(self.priority_queue) == 0

    def length(self):
        return len(self.priority_queue)

    def __str__(self):
        return str(self.priority_queue)
