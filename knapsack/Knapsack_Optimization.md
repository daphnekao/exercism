# Knapsack Optimization
## Prompt

Copied from [Exercism](https://exercism.io/my/solutions/7f6af07fb971484da38e9cc67312fc25):

Bob is a thief. After months of careful planning, he finally manages to crack
the security systems of a high-class apartment.

In front of him are many items, each with a value (v) and weight (w). Bob, of
course, wants to maximize the total value he can get; he would gladly take all
of the items if he could. However, to his horror, he realizes that the
knapsack he carries with him can only hold so much weight (W).

Given a knapsack with a specific carrying capacity (W), help Bob determine the
maximum value he can get from the items in the house. Note that Bob can take
only one of each item.

All values given will be strictly positive. Items will be represented as a
list of pairs, `w_i` and `v_i`, where the first element `w_i` is the weight of
the ith item and `v_i` is the value for that item.

For example:

Items:

```
[
    { "weight": 5, "value": 10 },
    { "weight": 4, "value": 40 },
    { "weight": 6, "value": 30 },
    { "weight": 4, "value": 50 }
]
```

Knapsack Limit: 10

For the above, the first item has weight 5 and value 10, the second item has
weight 4 and value 40, and so on.

In this example, Bob should take the second and fourth item to maximize his
value, which, in this case, is 90. He cannot get more than 90 as his knapsack
has a weight limit of 10.

# Approach

## It sounds so easy in theory...
My first instinct was to:

    1. Take all subsets of items weighing up to 10 lbs.
    2. Compute each subset's value.
    3. Return the maximum value from among them.

This method worked fine when there were only four items, but it got unwieldy
as the number of items grew. I also didn't know how to do this without
importing a math or combinatorics library.

My next idea was to partition the knapsack's weight limit. In the prompt's example where `W = 10`:

```
10 = 9 + 1
     8 + 2
     7 + 3
     6 + 4
     5 + 5
```

There could be a way to solve the smaller problems where the weight limit was
only 1 or 2 lbs, then use those answers to solve for progressively larger
weight limits.

To get unstuck, I did some research. This article helped me see
how I was on the right track but missing some pieces:

[How to Solve the Knapsack Problem with Dynamic Programming](https://medium.com/@fabianterh/how-to-solve-the-knapsack-problem-with-dynamic-programming-eb88c706d3cf)
by Fabian Terh

After reading the article, I manually worked out some examples (with mistakes)
until I understood this particular solution:

![Scratchwork-1](https://github.com/daphnekao/exercism/blob/main/knapsack/images/Scratchwork-1.JPG)
![Scratchwork-2](https://github.com/daphnekao/exercism/blob/main/knapsack/images/Scratchwork-2.JPG)

## ...but how does it work in practice?

[[This section is in progress.]]

1. Keep track of your work in a table.
1. First work with item 1.
1. Blah
1. Blah
What would be the total value if we left it out?
Ans: Whatever it was before with i - 1 items.
What would be the total value if we added it?
Ans: current item's value + max value from the sub-knapsack of weight j - current item's weight.
We can consider adding it to the knapsack, so compare.


|          | weightless | 1 lb | 2 lb | 3 lb | 4 lb | 5 lb | 6 lb | 7 lb |  8b |  9 lb |  10 lb |
|----------|------------|------|------|------|------|------|------|------|-----|-------|--------|
| no items | 0          | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0   | 0     | 0      |
| item 1   | 0          | 0    | 0    | 0    | 0    | 10   | 10   | 10   | 10  | 10    | 10     |
| item 2   | 0          | 0    | 0    | 0    | 40   | 40   | 40   | 40   | 40  | 50    | 50     |
| item 3   | 0          | 0    | 0    | 0    | 40   | 40   | 40   | 40   | 40  | 50    | 70     |
| item 4   | 0          | 0    | 0    | 0    | 50   | 50   | 50   | 50   | 90  | 90    | 90     |


# Further Considerations

- I think we can shave off some time by computing only the last cell (bottom
right-hand corner) of the last row rather than the entire row.
- For a huge knapsack and many items, this brute force approach could take much time and space. Is there a more efficient way to go about it? I suspect we wouldn't need to fill out the entire table but rather key cells that would lead us to the final cell.
- What happens if there are duplicate items and the thief can take more than
one of a kind?


