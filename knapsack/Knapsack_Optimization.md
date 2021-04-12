# Knapsack Optimization
## Prompt

Taken from [Exercism](https://exercism.io/my/solutions/7f6af07fb971484da38e9cc67312fc25):

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

For the above, the first item has weight 5 and value 10, the second item has weight 4 and value 40, and so on.

In this example, Bob should take the second and fourth item to maximize his value, which, in this case, is 90. He cannot get more than 90 as his knapsack has a weight limit of 10.

# Approach

## It sounds so easy in theory...
My first instinct was to:
    1. Take all subsets of items weighing up to 10 lbs.
    2. Compute each subset's value.
    3. Return the maximum value from among them.

This method works fine when there are only four items, but it quickly got unwieldy as the number of items grew.

My next idea was to partition the knapsack's weight limit. In the prompt's example where `W = 10`:

10 = 9 + 1
8 + 2
7 + 3
6 + 4
5 + 5

and 9 = 8 + 1
7 + 3
6 + 2
5 + 4

and so on...

There seemed to be a way to find solutions for when the weight limit was just 1 and 2, then recursively construct the solution for larger and larger weights until we finally had the solution for 10 lbs.

I got stuck here and did what I normally do when solving a problem on a deadline: I did some research. Luckily, this article helped me see how I was on the right track but missing a few pieces:

https://medium.com/@fabianterh/how-to-solve-the-knapsack-problem-with-dynamic-programming-eb88c706d3cf

I read the article and manually worked out some examples until I understood this particular solution: (Insert pictures)

## ...but how does it work in practice?

[[Fill in explanation]]



# Further Considerations
- I think we can shave off some time by computing only the last cell (bottom
right-hand corner) of the last row rather than the entire row.
- For a huge knapsack and many items, the
- What happens if there are duplicate items and the thief can take more than
one of a kind?

# Acknowledgments

