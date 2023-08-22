class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # 贪心算法，贪心算法的思路是每次尽可能的执行最优解，以达到全局最优解
        # 思路，一开始购买的水算作初始总数值，然后在循环中将每次整除得到能换到的水加入总数，然后再将能换到的水加上之前购买的水取模换水的条件后的水瓶赋值给当前拥有的水瓶
        total = numBottles
        while numBottles > numExchange:
            newBottles = numBottles // numExchange
            total += newBottles
            numBottles = newBottles + numBottles % numExchange
        return total


solution = Solution()
numBottles = 15
numExchange = 4
print(solution.numWaterBottles(numBottles, numExchange))
