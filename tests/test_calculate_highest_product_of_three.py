from unittest import *


class TestCalculateHighestProductOfThree(TestCase):

    def setUp(self):
        import sys
        sys.path.append("..")
        from src import calculate_highest_product_of_three as src
        self.calculate_highest_product_of_three = src.calculate_highest_product_of_three

    def test_valid_lists(self):
        self.assertEqual(self.calculate_highest_product_of_three([-100, 1, -10, 0, 2, 5, 9]), 9000)
        self.assertEqual(self.calculate_highest_product_of_three([0, 1, 3, 7, -2, 7, -8]), 147)
        self.assertEqual(self.calculate_highest_product_of_three([-1, 2, 3]), -6)
        self.assertEqual(self.calculate_highest_product_of_three([1, 10, 2, 6, 5, 3]), 300)

    def test_lists_with_invalid_items(self):
        self.assertRaises(TypeError, self.calculate_highest_product_of_three, [-10, 1, -10, 0, 2, 5, 'abc'])
        self.assertRaises(TypeError, self.calculate_highest_product_of_three, [-10, 1, -10, 0, 2, 5, None])
        self.assertRaises(TypeError, self.calculate_highest_product_of_three, [-10, 1, -10, 0, 2, 5, [2, 3, 4, 5]])

    def test_invalid_lists(self):
        self.assertRaises(TypeError, self.calculate_highest_product_of_three, ' ')
        self.assertRaises(TypeError, self.calculate_highest_product_of_three, dict())
        self.assertRaises(TypeError, self.calculate_highest_product_of_three, None)

    def test_invalid_list_length(self):
        self.assertRaises(ValueError, self.calculate_highest_product_of_three, [])
        self.assertRaises(ValueError, self.calculate_highest_product_of_three, [1])
        self.assertRaises(ValueError, self.calculate_highest_product_of_three, [1, 2])

if __name__ == '__main__':
    main()
