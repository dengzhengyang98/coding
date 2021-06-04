class Solution:
    def coinChange(self, coins, amount):
        coins.sort(reverse=True)
        result = []
        for i in range(len(coins)):
            self.greedy(coins, amount, i, 0, result)
        return len(result)

    def greedy(self, coins, amount, index, cur, result):
        if cur == amount:
            result
            return

        if cur > amount:
            return

        if cur < amount:
            for j in range(index, len(coins)):
                cur += coins[j]
                result.append(coins[j])
                self.greedy(coins, amount, j, cur, result)
                cur -= result.pop()

s = Solution()
print(s.coinChange([2], 3))