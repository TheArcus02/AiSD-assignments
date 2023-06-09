import numpy as np
import matplotlib.pyplot as plt


def knapSack(max_weight, weights, values, num_items):  # not optimized
    K = [[0 for x in range(max_weight + 1)] for x in range(num_items + 1)]

    # Build table K[][] in bottom up manner
    for i in range(num_items + 1):
        for weight in range(max_weight + 1):
            if i == 0 or weight == 0:
                K[i][weight] = 0
            elif weights[i-1] <= weight:
                K[i][weight] = max(values[i-1]
                                   + K[i-1][weight-weights[i-1]],
                                   K[i-1][weight])
            else:
                K[i][weight] = K[i-1][weight]

    return K[num_items][max_weight]


# optimized for space
def knapSackDynamic(max_weight: int, weights: list[int], values: list[int], num_items: int):

    dp = [0 for _ in range(max_weight + 1)]

    for i in range(1, num_items + 1):

        for current_weight in range(max_weight, 0, -1):
            if weights[i-1] <= current_weight:

                dp[current_weight] = max(
                    dp[current_weight], dp[current_weight - weights[i-1]] + values[i-1])
    return dp[max_weight]


def knapSackGreedy(max_weight: int, weights: list[int], values: list[int], num_items: int):
    items = list(zip(weights, values))
    items.sort(key=lambda x: x[1]/x[0], reverse=True)

    total_value = 0
    remaining_weight = max_weight

    for item in items:
        weight = item[0]
        value = item[1]

        if remaining_weight >= weight:
            # If the item can be accommodated in the knapsack, add it
            total_value += value
            remaining_weight -= weight

    return total_value


print(knapSack(8, [3, 2, 4, 3, 1], [5, 3, 4, 4, 2], 5))
