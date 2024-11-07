from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 数组大小为 amount + 1，初始值也为 amount + 1
        dp = [amount + 1] * (amount + 1)

        dp[0] = 0
        # base case
        # 外层 for 循环在遍历所有状态的所有取值
        for i in range(len(dp)):
            # 内层 for 循环在求所有选择的最小值
            for coin in coins:
                # 子问题无解，跳过
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], 1 + dp[i - coin])
        return -1 if dp[amount] == amount + 1 else dp[amount]


if __name__ == "__main__":
    solution = Solution()
    coins = [1, 2, 5]
    amount = 8
    result = solution.coinChange(coins, amount)
    print(f"最少硬币数: {result}")
