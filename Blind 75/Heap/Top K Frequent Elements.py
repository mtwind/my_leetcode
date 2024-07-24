from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # make freq dict and count distinct nums
        freq = Counter(nums)
        count = len(freq)
        heap, free = [None] * count, 0
        for key, val in freq.items():
            arr = [key, val]
            heap = self.insert(heap, arr, free)
            free += 1
        result = [None] * k
        for i in range(k):
            arr = self.getFirst(heap, free)
            free -= 1
            result[i] = arr[0]
        return result
    
    # iterate through freq map and add the frequencies to a max heap
    # get the first k elements
    def insert(self, heap: List[int], val: List[int], free: int) -> List[int]:
        if heap[0] is None:
            heap[0] = val
            return heap
        heap[free], parent = val, int((free - 1) / 2)
        while parent >= 0 and heap[parent][1] < val[1]:
            temp, heap[parent] = heap[parent], val
            heap[free], free = temp, parent
            parent = int((free - 1) / 2)
        return heap
        
    def getFirst(self, heap: List[int], free: int) -> List[int]:
        value, heap[0], heap[free-1], index = heap[0], heap[free-1], None, 0
        left = (2 * index) + 1 if (2 * index) + 1 < free - 1 else -1
        right = (2 * index) + 2 if (2 * index) + 2 < free - 1 else -1
        if left == -1:
            return value
        side = left if right == -1 or heap[right][1] < heap[left][1] else right
        while heap[index][1] < heap[side][1]:
            temp, heap[index] = heap[index], heap[side]
            heap[side], index = temp, side
            left = (2 * index) + 1 if (2 * index) + 1 < free - 1 else -1
            right = (2 * index) + 2 if (2 * index) + 2 < free - 1 else -1
            if left == -1:
                return value
            side = left if right == -1 or heap[right][1] < heap[left][1] else right
        return value