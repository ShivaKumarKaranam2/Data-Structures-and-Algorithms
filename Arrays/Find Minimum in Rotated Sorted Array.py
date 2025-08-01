"""153. Find Minimum in Rotated Sorted Array

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

"""
class Solution:
    def findMin(self, nums):
        n = len(nums)
        low = 0
        high = n-1
        min_element = float('inf')
        while low <= high:
            mid = (low+high)//2
            if nums[low] < nums[high]:
                min_element = min(min_element,nums[low])
                break
            elif nums[low] <= nums[mid]:
                min_element = min(min_element,nums[mid])
                low = mid+1
            else:
                high = mid-1
                min_element = min(min_element,nums[mid])
        return min_element


#Example
if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    solution = Solution()
    result = solution.findMin(nums)
    print(result)