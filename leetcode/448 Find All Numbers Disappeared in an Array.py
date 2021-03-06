class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while nums[i] != i+1 and nums[nums[i]-1] != nums[i]:
                temp1 = nums[i]
                temp2 = nums[nums[i]-1]
                nums[i] = temp2
                nums[temp1-1] = temp1
                # print(nums)
        return [i+1 for i in range(len(nums)) if i+1 != nums[i]]
        
"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""
