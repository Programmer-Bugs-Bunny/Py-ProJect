class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high + 1) // 2 - low // 2


solution = Solution()
low = 798273637
high = 970699661
print(solution.countOdds(low, high))
