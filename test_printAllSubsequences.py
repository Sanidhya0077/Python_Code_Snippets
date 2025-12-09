import unittest

from your_module import all_subsequences  # change 'your_module' to your file name (without .py)


class TestAllSubsequences(unittest.TestCase):

    def test_three_elements(self):
        nums = [1, 2, 3]
        result = all_subsequences(nums)

        expected = [
            [], [1], [2], [3],
            [1, 2], [1, 3], [2, 3],
            [1, 2, 3],
        ]

        # order may differ, so compare as sorted lists
        self.assertEqual(sorted(result), sorted(expected))
        # also check count = 2^n
        self.assertEqual(len(result), 2 ** len(nums))

    def test_empty_list(self):
        nums = []
        result = all_subsequences(nums)

        expected = [[]]  # only the empty subsequence
        self.assertEqual(result, expected)

    def test_single_element(self):
        nums = [7]
        result = all_subsequences(nums)

        expected = [[], [7]]
        self.assertEqual(sorted(result), sorted(expected))

    def test_with_duplicates(self):
        nums = [1, 1]
        result = all_subsequences(nums)

        # subsequences (order and duplicates allowed):
        # [], [1] (first), [1] (second), [1,1]
        expected = [[], [1], [1], [1, 1]]

        # convert to multisets via sorted of tuples to ignore ordering of the outer list
        self.assertEqual(sorted(map(tuple, result)),
                         sorted(map(tuple, expected)))


if __name__ == "__main__":
    unittest.main()
