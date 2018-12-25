class Solution:
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices or k==0:
            return 0

        # Simple optimisation
        if k >= len(prices)/2:
            return sum(
                a-b
                for a,b in zip(prices[1:], prices[:-1])
                if a>b
            )

        #: Max profit when there are <index> transactions
        global_max = [0] * (k+1)

        #: Max profit when there are <index> transactions and last transaction
        # ends at the last day.
        local_max = [0] * (k+1)

        for i in range(1, len(prices)):
            #i: Prices with length i+1 (2, 3, ..., length(prices))

            #: Newly appended price's diff with previous one
            diff = prices[i] - prices[i-1]

            # Update local_max[:k] and global_max[:k]
            for j in range(k, 0, -1):
                local_max[j] = max(local_max[j], global_max[j-1]) + diff
                global_max[j] = max(local_max[j], global_max[j])

        return global_max[k]


def main():
    cases = [
        (2, [1,3,2,6,5,0,3]),
    ]
    for k, prices in cases:
        print(Solution().maxProfit(k, prices))


if __name__ == '__main__':
    main()

