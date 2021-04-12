
def maximize_knapsack_value(weight_limit, items):
    """
    :param weight_limit: upper bound on how many pounds the knapsack can hold
    :type weight_limit: `int`
    :param items: list of weight-value pairs
    :type items: `list` of `dict`
    :returns:
        n x w matrix where row i, column j holds the greatest total value
        possible when selecting from among items 1, 2, 3, ... i under a weight
        restriction of j, and where 1 <= i <= n, 1 <= j <= w.
    :return type: `list` of `list`

    Example data:

    weight_limit = 10

    items = [
        { "weight": 5, "value": 10 },
        { "weight": 4, "value": 40 },
        { "weight": 6, "value": 30 },
        { "weight": 4, "value": 50 }
    ]

    Example output:

    [
        [ 0, 0, 10, 0 ],
        [ 0, 40, 40, 50 ],
        [ 0, 5, 50, 85 ],
    ]

    """
    # Create the matrix shell, including a row for 0 items and a column for 0 lbs
    # Explain why we leave the zero row and zero column as-is.
    matrix = [ [ 0 for i in range(weight_limit + 1)] for j in range(len(items) + 1) ]

    # Populate the matrix.
    for i in range(1, len(items) + 1):
        row_i = matrix[i]
        item = items[i - 1]
        item_weight = item["weight"]
        item_value = item["value"]
        for j in range(1, weight_limit + 1):
            # What would be the total value if we left it out?
            # Ans: Whatever it was before with i - 1 items.
            best_value_so_far = matrix[i - 1][j]
            # What would be the total value if we added it?
            # Ans: current item's value + max value from the sub-knapsack of weight j - current item's weight.
            potential_new_value = item_value + matrix[i - 1][j - item_weight]
            # Default to keeping whatever it was before with i - 1 items.
            row_i[j] = best_value_so_far
            if item_weight <= j:
                # We can consider adding it to the knapsack, so compare.
                if potential_new_value > best_value_so_far:
                    row_i[j] = potential_new_value

    # Uncomment to see the matrix.
    # print("Matrix of Optimal Values")
    # for row in matrix:
    #     print(row)

    # The final answer lies in the bottom right cell.
    return matrix[len(items)][weight_limit]

print("Answer:")
print(maximize_knapsack_value(10, [{ "weight": 5, "value": 10 }, { "weight": 4, "value": 40 }, { "weight": 6, "value": 30 }, { "weight": 4, "value": 50 }, { "weight": 2, "value": 5 }, { "weight": 1, "value": 35 }]))
