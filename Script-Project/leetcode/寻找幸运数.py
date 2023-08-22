from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        number_dist = {}
        for i in arr:
            if number_dist.get(i):
                number_dist[i] += 1
            else:
                number_dist[i] = 1
        number = -1
        for i in arr:
            if i == number_dist[i]:
                number = max(number, i)
        return number


solution = Solution()
arr = [1,2,2,3,3,3]
print(solution.findLucky(arr))
