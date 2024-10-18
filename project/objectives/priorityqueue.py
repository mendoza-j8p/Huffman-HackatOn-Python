class PriorityQueue:
    def __init__(self, compare=lambda x : x):
        self.pq = [] # Empty list
        self.compare = compare # Function used to compare

    def push(self, value):
        """
            Push an element to the PriorityQueue.
            @params value: Element to push to the PQ.
            @returns: None
        """
        self.pq.append(value)
        self.pq.sort(key=self.compare)

    def pop(self):
        """
            Returns and removes the first element on the queue.
            @returns: First element of the queuea
        """
        if not self.pq:
            return None
        
        return self.pq.pop(0)


    def isEmpty(self):
        """
            Check if the PriorityQueue is empty or not.
            @returns: True if PriorityQueue is empty, otherwise false
        """
        return len(self.pq) == 0

    def length(self):
        """
            Returns the amount of elements in the PriorityQueue
            @returns: The amount of elements in the PriorityQueue
        """
        return len(self.pq)

    def __str__(self):
        return str([f for n,f in self.pq])
