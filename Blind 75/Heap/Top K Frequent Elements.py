class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # loop through and count freq
        # also count num of distinct numbers
        # iterate through freq map and add the frequencies to a max heap
        # get the first k elements
        