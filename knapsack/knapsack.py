
def maximize_knapsack_value(weight_limit, items):
    """
    :param weight_limit: upper bound on how many pounds the knapsack can hold
    :type weight_limit: `int`
    :param items: list of weight-value pairs
    :type items: `list` of `dict`
    :returns: greatest possible value that the knapsack can hold
    :return type: `int`

    Example:

    weight_limit = 10

    items = [
        { "weight": 5, "value": 10 },
        { "weight": 4, "value": 40 },
        { "weight": 6, "value": 30 },
        { "weight": 4, "value": 50 }
    ]

    Generates this matrix:
[
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 10, 10, 10, 10, 10, 10],
    [0, 0, 0, 0, 40, 40, 40, 40, 40, 50, 50],
    [0, 0, 0, 0, 40, 40, 40, 40, 40, 50, 70],
    [0, 0, 0, 0, 50, 50, 50, 50, 90, 90, 90]
]

    Yields this answer:
    90

    """

    # Create appropriately sized matrix. Fill it with zeros to begin.
    num_items = len(items)
    matrix = [ [ 0 for i in range(weight_limit + 1)] for j in range(num_items + 1) ]

    # Populate the matrix.
    for i in range(1, num_items + 1):
        row_i = matrix[i]
        item = items[i - 1]
        item_weight = item["weight"]
        item_value = item["value"]
        for j in range(1, weight_limit + 1):
            best_value_so_far = matrix[i - 1][j]
            potential_new_value = item_value + matrix[i - 1][j - item_weight]
            row_i[j] = best_value_so_far
            if item_weight <= j:
                if potential_new_value > best_value_so_far:
                    row_i[j] = potential_new_value

    # Uncomment to see the matrix.
    # print("Matrix of Optimal Values")
    # for row in matrix:
    #     print(row)

    # The final answer lies in the bottom right cell.
    return matrix[num_items][weight_limit]
