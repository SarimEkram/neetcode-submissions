class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxLen = len(heights) - 1
        right = len(heights) - 1
        left = 0
        output = 0

        while left < right:

            if heights[left] < heights[right]:
                print(heights[left])


                if output < heights[left] * maxLen:
                    output = heights[left] * maxLen
                    print(output)

                left += 1
                maxLen -= 1
            else:

                if output < heights[right] * maxLen:
                    output = heights[right] * maxLen

                right -= 1
                maxLen -= 1
        return output