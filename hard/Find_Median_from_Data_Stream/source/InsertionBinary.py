class MedianFinder:

    def __init__(self):
        # set an global array
        self.nums = list()

    def addNum(self, num: int) -> None:
        # simply append the input if the array is empty
        if not self.nums:
            self.nums.append(num)
            return
            # run the binary search until left and right converges
        l = 0
        r = len(self.nums) - 1
        while l < r:
            m = (l + r) // 2
            # insert next to the pivot if the input is equal to the pivot
            if self.nums[m] == num:
                self.nums.insert(m, num)
                return
            elif self.nums[m] < num:
                l = m + 1
            else:
                r = m - 1
                # if the input is larger than the whole array ex) [_,_,_,_,_,L] + [x]
        if self.nums[l] < num:
            self.nums.insert(l + 1, num)

        # if the input belongs in the middle of the array ex) [_,_,_,_,_,x,L]
        else:
            self.nums.insert(l, num)

    def findMedian(self) -> float:
        # return the median
        mid = (0 + len(self.nums) - 1) // 2
        if (len(self.nums) - 1) % 2 != 0:
            return (self.nums[mid] + self.nums[mid + 1]) / 2
        else:
            return self.nums[mid]