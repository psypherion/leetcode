from typing import List

"""
O(n^2) -> Traversing array
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target: 
                    return i, j


if __name__ == "__main__":
    sol: object = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(f"Numbers : {nums}\nTarget : {target}")
    print(f"Solution : {sol.twoSum(nums, target)}")
