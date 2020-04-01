def maxProfit(nums):
    """

    :param nums:
    :return:
    """
    profit = 0
    for i in range(len(nums) - 1):
        sub = max(nums[i + 1:]) - nums[i]
        profit = max(sub, profit)
    return profit


if __name__ == '__main__':
    nums = [7, 1, 5, 3, 6, 4]
    print(maxProfit(nums))
