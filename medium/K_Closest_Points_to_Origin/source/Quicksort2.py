class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def dist(index):
            return sqrt(pow(points[index][0], 2) + pow(points[index][1], 2))

        def partition(left, right):
            pivot = left
            left += 1

            while True:
                while left < right and dist(left) < dist(pivot):
                    left += 1
                while left <= right and dist(right) >= dist(pivot):
                    right -= 1

                if left >= right:
                    break
                points[left], points[right] = points[right], points[left]

            points[pivot], points[right] = points[right], points[pivot]
            return right

        def quicksort(left, right, K):
            if left >= right:
                return

            pivot = random.randint(left, right)
            points[pivot], points[left] = points[left], points[pivot]

            mid = partition(left, right)

            if K < (mid - left + 1):
                quicksort(left, mid - 1, K)
            elif K > (mid - left + 1):
                quicksort(mid + 1, right, K - (mid - left + 1))

        quicksort(0, len(points) - 1, K)
        return points[:K]



