"""
Leetcode 31 :Next Permutation

A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]




My Reflection :
    The next permutation is the smallest lexicographically greater permutation of the array.
    so, We have to find the that permutation

    Steps:
    1. We have to find the pivot index from reverse ,which satisfies the arr[i] < arr[i+1].
    2. Find the Right Most Element to pivot that should > arr[pivot] from last to pivot.
    3. Reverse the elements from pivot+1 to end .


"""

class Solution:
    def nextPermutation(self,arr):
        pivot = -1

        #1. We have to find the pivot index from reverse ,which satisfies the arr[i] < arr[i+1].
        for i in range(len(arr)-2,-1,-1):
            if arr[i] < arr[i+1]:
                pivot = i
                break
        
        #Edge case
        if pivot == -1:
            arr.reverse()
            return arr
        
        #  2. Find the Right Most Element to pivot that should > arr[pivot] from last to pivot.
        for i in range(len(arr)-1,pivot,-1):
            if arr[i] > arr[pivot]:
                arr[i],arr[pivot] = arr[pivot],arr[i]
                break

        #3. Reverse the elements from pivot+1 to end .

        left, right = pivot+1, len(arr)-1
        while left < right:
            arr[left],arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

        return arr
    
if __name__ == "__main__":
    solution = Solution()
    arr = [3,2,1]
    result = solution.nextPermutation(arr)
    print(f"The next permutation is {result}")



        

        