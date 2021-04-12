import unittest

from knapsack import maximize_knapsack_value

class KnapsackTest(unittest.TestCase):


    def test_prompt_example(self):
        weight_limit = 10
        items = [
            {"weight": 5, "value": 10},
            {"weight": 4, "value": 40},
            {"weight": 6, "value": 30},
            {"weight": 4, "value": 50},
        ]
        expected_value = 90
        self.assertEqual(maximize_knapsack_value(weight_limit, items), expected_value)


    # def test_6_items(self):
    #     weight_limit = 10
    #     items = [
    #         { "weight": 5, "value": 10 },
    #         { "weight": 4, "value": 40 },
    #         { "weight": 6, "value": 30 },
    #         { "weight": 4, "value": 50 },
    #         { "weight": 2, "value": 5 },
    #         { "weight": 1, "value": 35 }
    #     ]
    #     expected_value = 125
    #     self.assertEqual(maximize_knapsack_value(weight_limit, items), expected_value)

    # def test_zero_items(self):
    #     weight_limit = 10
    #     items = []
    #     expected_value = 0
    #     self.assertEqual(maximize_knapsack_value(weight_limit, items), expected_value)


    # def test_one_item(self):
    #     weight_limit = 1
    #     items = [{"weight":1 , "value": 20}]
    #     expected_value = 20
    #     self.assertEqual(maximize_knapsack_value(weight_limit, items), expected_value)

if __name__ == "__main__":
    unittest.main()
