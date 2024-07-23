class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # loop through and count freq
        # also count num of distinct numbers
        freq = {}
        count = 0
        for num in nums:
            if num not in freq:
                freq[num] = 1
                count += 1
            else:
                freq[num] += 1
        print(f"{freq}\ncount: {count}")

        heap = [None] * 3
        print(heap)
        free = 0
        for key, val in freq.items():
            arr = [key, val]
            heap = self.insert(heap, arr, free)
            print(f"heap: {heap}")
            free += 1


        
        # iterate through freq map and add the frequencies to a max heap
        # get the first k elements
    def insert(self, heap: List[int], val: List[int], free: int) -> List[int]:
        if heap[0] is None:
            heap[0] = val
            return heap

        heap[free] = val
        parent = int((free - 1) / 2)
        
        while parent >= 0 and heap[parent][1] < val[1]:
            temp = heap[parent]
            heap[parent] = val
            heap[free] = temp
            # print(f"{val[1]} inserted at {parent}")
            free = parent
            parent = (free - 1) / 2
            # print(f"    nums: {heap}")
        return heap
        
    def getFirst(self, heap: List[int], free: int) -> List[int]:
        value = heap[0]
        heap[0] = heap[free-1]
        index = 0
        left = (2 * index) + 1
        right = (2 * index) + 2
        side = left if heap[left][1] > heap[right][1] else right

        while heap[index][1] < heap[side][1]:
            # swim down
            print()

        return value


