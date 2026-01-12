from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        k = 1  # index for next unique element

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k
    

# Example usage:
solution = Solution()   
nums = [0,0,1,1,1,2,2,3,3,4]
k = solution.removeDuplicates(nums)
print(f"Length of array after removing duplicates: {k}")
print(f"Array after removing duplicates: {nums[:k]}")
# Output:
# Length of array after removing duplicates: 5
# Array after removing duplicates: [0, 1, 2, 3, 4]

