class PriorityQueue:
    def __init__(self, compare=lambda x : x):
        self.pq = [] # Empty list
        self.compare = compare # Function used to compare

    def push(self, value):
        self.pq.append(value)
        self.pq.sort(key=self.compare)

    def pop(self):
        return self.pq.pop(0) if not self.isEmpty() else None

    def isEmpty(self):
        return len(self.pq) == 0

    def length(self):
        return len(self.pq)

    def __str__(self):
        return str(self.pq)
