from typing import List


class Solution:
    def __init__(self):
        self.memo = []

    def coinChange(self, coins: List[int], amount: int) -> int:
        self.memo = [-666] * (amount + 1)
        # 备忘录初始化为一个不会被取到的特殊值，代表还未被计算
        return self.dp(coins, amount)

    def dp(self, coins, amount):
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        # 查备忘录，防止重复计算
        if self.memo[amount] != -666:
            return self.memo[amount]

        res = float('inf')
        for coin in coins:
            # 计算子问题的结果
            subProblem = self.dp(coins, amount - coin)
            # 子问题无解则跳过
            if subProblem == -1:
                continue
            # 在子问题中选择最优解，然后加一
            res = min(res, subProblem + 1)
        # 把计算结果存入备忘录
        self.memo[amount] = res if res != float('inf') else -1
        return self.memo[amount]


if __name__ == "__main__":
    solution = Solution()
    coins = [1, 2, 5]
    amount = 18
    result = solution.coinChange(coins, amount)
    print(f"最少硬币数: {result}")  # 期望输出: 3 (11 = 5 + 5 + 1)
