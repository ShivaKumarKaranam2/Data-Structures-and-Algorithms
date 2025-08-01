"""
leetcode:
11. Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0 
        l,r = 0,len(height)-1
        while l < r:
            area = (r-l)*min(height[l],height[r])
            res = max(res,area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res
#Example
if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    solution = Solution()
    result = solution.maxArea(height)
    print(result)