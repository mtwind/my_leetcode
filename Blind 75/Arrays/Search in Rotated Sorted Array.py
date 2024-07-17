class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) <= 2:
            if target in nums:
                print(f"found {target}")
                return nums.index(target)
            else:
                print(f"returned -1")
                return -1


        # [4,5,6,7,0,1,2], target 2
        # move 4 to middle and record index
            # [5,6,7,4,0,1,2]
            # index = 3
        mid = int(len(nums)/2)
        temp = nums[0]
        if temp is target:
            return 0
        del nums[0]
        nums.insert(mid, temp)
        index = mid
        # determine left and right
        right, left = nums[mid + 1], nums[mid-1]
        print("\n")
        
        print(nums)
        print(f"    temp: {temp}")
        print(f"    left: {left}")
        print(f"    right: {right}")
        # if 4 < left and 4 > right, search left if target > 4 and right is target < 4
        # 4 > target so search right [4,0,1,2]
        if temp < left and temp > right:
            if target >= temp:
                # search left
                print(f"    going left 1, {index}")
                print(f"    nums: {nums[:mid]}")
                num = self.search(nums[:mid], target)
                return num + 1 if num is not -1 else -1
            else:
                # search right
                print(f"    going right 1, {index}")
                print(f"    nums: {nums[mid+1:]}")
                num = self.search(nums[mid+1:], target)
                return num + index if num is not -1 else -1
        # move 4 to middle and record index
            # [0,1,4,2]
            # index = 2
        # if 4 > left and 4 > right, search left if target <= left and right if target >= right
        # target >= right so search right [4,2]
            # return index 1
        if temp > left and temp > right:
            if target < temp:
                # search left
                print(f"    going left 2, {index}")
                print(f"    nums: {nums[:mid]}")
                num = self.search(nums[:mid], target)
                return num + 1 if num is not -1 else -1
            else:
                # search right
                print(f"    going right 2, {index}")
                print(f"    nums: {nums[mid+1:]}")
                num = self.search(nums[mid+1:], target)
                return num + index if num is not -1 else -1
        # [4,5,6,7,8,9,0,1,2] -> [5,6,7,8,4,9,0,1,2]
        # if temp < left and temp < right
        if temp < left and temp < right:
            if target > temp:
                # search left
                print(f"    going left 3, {index}")
                print(f"    nums: {nums[:mid]}")
                num = self.search(nums[:mid], target)
                return num + 1 if num is not -1 else -1
            else:
                print()
                # search right
                print(f"    going right 3, {index}")
                print(f"    nums: {nums[mid+1:]}")
                num = self.search(nums[mid+1:], target)
                return num + index if num is not -1 else -1

        
        return 0