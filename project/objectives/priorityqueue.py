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
        pass

    def pop(self):
        """
            Returns and removes the first element on the queue.
            @returns: First element of the queue
        """
        return 0

    def isEmpty(self):
        """
            Check if the PriorityQueue is empty or not.
            @returns: True if PriorityQueue is empty, otherwise false
        """
        return False

    def length(self):
        """
            Returns the amount of elements in the PriorityQueue
            @returns: The amount of elements in the PriorityQueue
        """
        return 0

    def __str__(self):
        return str([f for n,f in self.pq])
