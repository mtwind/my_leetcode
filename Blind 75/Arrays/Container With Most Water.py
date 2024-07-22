class Solution:
    def maxArea(self, height: List[int]) -> int:
        result, n = 0, len(height)
        i, j  = 0, n-1
        while i < j:
            jval = height[j]
            ival = height[i]
            val = (j - i) * min(ival, jval)
            result = val if val > result else result
            if ival <= jval:
                i += 1
            else: 
                j -= 1
        return result
            
            


# # optimized brute force still fails
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         # areaLeft, areaRight = [i * height(i), (n-i-1) * height(i)]
#         # [[0,8], [8, 56], [12, 36], [6,10], [20,20], [20,12], [48,16], [21,3], [56,0]]

#         # need to find indexes i and j with highest value = (j - i) * min(height[i], height(j)) 

#         # increasing list from left: [1,8] or [0,1] (indexes)
#         # decreasing list from right: [7,8] or [8,6] (indexes)
#         n = len(height)
#         left, right, i = [0], [n-1], 1
#         while i < n - i - 1:
#             if height[i] > height[left[-1]]:
#                 left.append(i)
#             if height[n-1-i] > height[right[-1]]:
#                 right.insert(0,n-1-i)
#             i += 1
#         mid = len(left)
#         left.extend(right)
#         result = 0
#         for i in range(mid):
#             for j in range(mid,len(left)):
#                 val = (left[j] - left[i]) * min(height[left[i]], height[left[j]])
#                 # print(f"val = ({j} - {i}) * min({height[left[i]]}, {height[left[j]]}) = {val}")
#                 result = val if val > result else result
#         return result