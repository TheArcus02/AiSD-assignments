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
