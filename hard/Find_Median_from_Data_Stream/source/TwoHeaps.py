class MedianFinder:

    def __init__(self):
        # set a max-heap that stores the smaller half of the numbers
        self.maxheap = list()
        # set a min-heap that stores the larger half of the numbers
        self.minheap = list()

    def addNum(self, num: int) -> None:

        # balance the max=heap and minheap so that max-heap can store one more element than min heap
        heapq.heappush(self.maxheap, -num)
        heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))
        if len(self.maxheap) < len(self.minheap):
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))

    def findMedian(self) -> float:
        # if the total length of the numbers are odd
        if len(self.maxheap) > len(self.minheap):
            # return the result from the max-heap
            return -self.maxheap[0]
        # if the total length of the numbers are even
        else:
            # return the median computed from both max-heap and min-heap
            return (-self.maxheap[0] + self.minheap[0]) / 2
