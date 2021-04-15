# Knapsack Optimization

## Prompt

Copied from [Exercism](https://exercism.io):

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

## Approach

### It sounds so easy in theory...
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
to solidify understanding:

![Scratchwork-1](https://github.com/daphnekao/exercism/blob/main/knapsack/images/Scratchwork-1.JPG)
![Scratchwork-2](https://github.com/daphnekao/exercism/blob/main/knapsack/images/Scratchwork-2.JPG)

### ...but how does it work in practice?

1. We keep track of our work in an `(n + 1) x (W + 1)` table where `n` is the number of items and `W` is the knapsack's weight limit.
1. First, we pick up item 1 and ask:
    1. Is item 1 light enough to fit in a smaller knapsack that holds just 1
    lb? How about 2 lbs? 8lbs?
    1. If yes, then add the item to the sub-knapsack. In our example, item 1
    weighs 5 lbs and is worth $10. That means that it can fit in any knapsack
    of size 5 lbs or more, and it definitely makes sense to nab those $10
    rather than leave it behind!
1. Next, we pick up item 2. It weighs 4 lbs and is worth $40. For each of
the weight limits between 1 lb and 10 lbs, we do a comparison. For example,
suppose we're wondering whether to add item 2 to a knapsack that can only hold
6 lbs.
    1. Is item 2 even light enough to fit? In this case, yes because
    `4 lbs < 6 lbs`. If it were too heavy, then we'd leave it behind and note
    that the 6 lb knapsack's optimal value is the same as it was when only
    item 1 was in the mix. (Same column, one row up.)
    1. Since it can fit, now we compute the potential value of combining item
    2, which weighs 4 lbs, with whatever items maximized the 2 lb knapsack's
    value (because 4 lbs + 2 lbs = 6 lbs).
    1. We compare this potential value to the optimal value determined before
    we even picked up item 2. The worse that could happen is that we maintain
    the old optimal value, right? (Same column, one row up.) Pick whichever
    value is greater, and you're on your way!
    1. Continue picking up items and making these comparisons until you're
    considering adding the last item to the big knapsack that weighs 10 lbs.
    Your decision here is the answer to the entire problem!


|          | weightless | 1 lb | 2 lb | 3 lb | 4 lb | 5 lb | 6 lb | 7 lb |  8b |  9 lb |  10 lb |
|----------|------------|------|------|------|------|------|------|------|-----|-------|--------|
| no items | 0          | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0   | 0     | 0      |
| item 1   | 0          | 0    | 0    | 0    | 0    | 10   | 10   | 10   | 10  | 10    | 10     |
| item 2   | 0          | 0    | 0    | 0    | 40   | 40   | 40   | 40   | 40  | 50    | 50     |
| item 3   | 0          | 0    | 0    | 0    | 40   | 40   | 40   | 40   | 40  | 50    | 70     |
| item 4   | 0          | 0    | 0    | 0    | 50   | 50   | 50   | 50   | 90  | 90    | 90     |


## Extensions, Improvements, and Edge Cases

- I think we can shave off some time by computing only the last cell (bottom
right-hand corner) of the last row rather than the entire row.
- For a huge knapsack and many items, this brute force approach could consume
much time and space. Is there a more efficient way? I suspect we wouldn't need
to fill out the entire table but rather keystone cells that would lead us to
the final cell.
- What happens if there are duplicate items and the thief can take more than
one of a kind?
- What about virtually weightless items that are worth a ton? (e.g., blank
check, rare baseball card)


## Running Tests

```
$ pytest knapsack_test.py
```
