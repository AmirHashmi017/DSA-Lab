import unittest
import funcs


class TestSortedMerge(unittest.TestCase):
    def test_sorted_merge_basic(self):
        self.assertEqual(funcs.SortedMerge([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])

    def test_sorted_merge_empty_first(self):
        self.assertEqual(funcs.SortedMerge([], [2, 4, 6]), [2, 4, 6])

    def test_sorted_merge_empty_second(self):
        self.assertEqual(funcs.SortedMerge([1, 3, 5], []), [1, 3, 5])

    def test_sorted_merge_both_empty(self):
        self.assertEqual(funcs.SortedMerge([], []), [])

    def test_sorted_merge_duplicates(self):
        self.assertEqual(
            funcs.SortedMerge([1, 3, 5, 5], [2, 4, 5, 6]), [1, 2, 3, 4, 5, 5, 5, 6]
        )

    def test_sorted_merge_negative_numbers(self):
        self.assertEqual(
            funcs.SortedMerge([-3, -1, 2], [-2, 0, 3]), [-3, -2, -1, 0, 2, 3]
        )

    def test_sorted_merge_different_lengths(self):
        self.assertEqual(
            funcs.SortedMerge([1, 2, 3], [4, 5, 6, 7, 8]), [1, 2, 3, 4, 5, 6, 7, 8]
        )


class TestSearchA(unittest.TestCase):
    def test_search_a_basic(self):
        self.assertEqual(funcs.SearchA([1, 2, 3, 4, 5], 3), [2])

    def test_search_a_multiple_occurrences(self):
        self.assertEqual(funcs.SearchA([1, 2, 3, 3, 5], 3), [2, 3])

    def test_search_a_no_occurrence(self):
        self.assertEqual(funcs.SearchA([1, 2, 3, 4, 5], 6), [])

    def test_search_a_empty_list(self):
        self.assertEqual(funcs.SearchA([], 1), [])

    def test_search_a_all_elements_same(self):
        self.assertEqual(funcs.SearchA([1, 1, 1, 1, 1], 1), [0, 1, 2, 3, 4])

    def test_search_a_negative_numbers(self):
        self.assertEqual(funcs.SearchA([-1, -2, -3, -4, -5], -3), [2])

    def test_search_a_mixed_numbers(self):
        self.assertEqual(funcs.SearchA([1, -2, 3, -4, 5], -4), [3])


class TestMinimum(unittest.TestCase):
    def test_minimum_basic(self):
        self.assertEqual(funcs.Minimum([3, 1, 4, 1, 5], 0, 4), 1)

    def test_minimum_single_element(self):
        self.assertEqual(funcs.Minimum([3, 1, 4, 1, 5], 2, 2), 2)

    def test_minimum_entire_array(self):
        self.assertEqual(funcs.Minimum([3, 1, 4, 1, 5], 0, 4), 1)

    def test_minimum_subarray(self):
        self.assertEqual(funcs.Minimum([3, 1, 4, 1, 5], 1, 3), 1)

    def test_minimum_negative_numbers(self):
        self.assertEqual(funcs.Minimum([-3, -1, -4, -1, -5], 0, 4), 4)

    def test_minimum_mixed_numbers(self):
        self.assertEqual(funcs.Minimum([3, -1, 4, -1, 5], 0, 4), 1)

    def test_minimum_starting_equals_ending(self):
        self.assertEqual(funcs.Minimum([3, 1, 4, 1, 5], 3, 3), 3)


class TestSort4(unittest.TestCase):
    def test_sort4_basic(self):
        self.assertEqual(funcs.Sort4([3, 1, 4, 1, 5]), [1, 1, 3, 4, 5])

    def test_sort4_empty_list(self):
        self.assertEqual(funcs.Sort4([]), [])

    def test_sort4_single_element(self):
        self.assertEqual(funcs.Sort4([1]), [1])

    def test_sort4_sorted_list(self):
        self.assertEqual(funcs.Sort4([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_sort4_reverse_sorted_list(self):
        self.assertEqual(funcs.Sort4([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_sort4_duplicates(self):
        self.assertEqual(funcs.Sort4([3, 3, 3, 3, 3]), [3, 3, 3, 3, 3])

    def test_sort4_negative_numbers(self):
        self.assertEqual(funcs.Sort4([-3, -1, -4, -1, -5]), [-5, -4, -3, -1, -1])

    def test_sort4_mixed_numbers(self):
        self.assertEqual(funcs.Sort4([3, -1, 4, -1, 5]), [-1, -1, 3, 4, 5])


class TestPalindromRecursive(unittest.TestCase):
    def test_palindrom_recursive_basic(self):
        self.assertTrue(funcs.PalindromRecursive("radar"))

    def test_palindrom_recursive_single_character(self):
        self.assertTrue(funcs.PalindromRecursive("a"))

    def test_palindrom_recursive_empty_string(self):
        self.assertTrue(funcs.PalindromRecursive(""))

    def test_palindrom_recursive_not_palindrome(self):
        self.assertFalse(funcs.PalindromRecursive("hello"))

    def test_palindrom_recursive_even_length_palindrome(self):
        self.assertTrue(funcs.PalindromRecursive("abba"))

    def test_palindrom_recursive_mixed_case(self):
        self.assertFalse(funcs.PalindromRecursive("Radar"))

    def test_palindrom_recursive_with_spaces(self):
        self.assertFalse(funcs.PalindromRecursive("a man a plan a canal panama"))

    def test_palindrom_recursive_special_characters(self):
        self.assertTrue(funcs.PalindromRecursive("!@##@!"))

    def test_palindrom_recursive_numeric_palindrome(self):
        self.assertTrue(funcs.PalindromRecursive("12321"))

    def test_palindrom_recursive_numeric_not_palindrome(self):
        self.assertFalse(funcs.PalindromRecursive("12345"))


class TestSearchB(unittest.TestCase):
    def test_search_b_basic(self):
        self.assertEqual(funcs.SearchB([1, 2, 3, 4, 5], 3), [2])

    def test_search_b_multiple_occurrences(self):
        self.assertEqual(funcs.SearchB([1, 2, 3, 3, 5], 3), [2, 3])

    def test_search_b_no_occurrence(self):
        self.assertEqual(funcs.SearchB([1, 2, 3, 4, 5], 6), [])

    def test_search_b_empty_list(self):
        self.assertEqual(funcs.SearchB([], 1), [])

    def test_search_b_negative_numbers(self):
        self.assertEqual(funcs.SearchB([-5, -4, -3, -2, -1], -3), [2])

    def test_search_b_mixed_numbers(self):
        self.assertEqual(funcs.SearchB([-4, -2, 0, 2, 4], 0), [2])

    def test_search_b_large_list(self):
        self.assertEqual(funcs.SearchB(list(range(1000)), 500), [500])

    def test_search_b_first_element(self):
        self.assertEqual(funcs.SearchB([1, 2, 3, 4, 5], 1), [0])

    def test_search_b_last_element(self):
        self.assertEqual(funcs.SearchB([1, 2, 3, 4, 5], 5), [4])


class TestSort10(unittest.TestCase):
    def test_sort10_basic(self):
        self.assertEqual(
            funcs.Sort10([10, -1, 9, 20, -3, -8, 22, 9, 7]),
            [-8, 7, -3, 9, -1, 9, 10, 20, 22],
        )

    def test_sort10_only_positive(self):
        self.assertEqual(funcs.Sort10([10, 9, 20, 22, 9, 7]), [7, 9, 9, 10, 20, 22])

    def test_sort10_only_negative(self):
        self.assertEqual(
            funcs.Sort10([-10, -9, -20, -22, -9, -7]), [-22, -20, -10, -9, -9, -7]
        )

    def test_sort10_empty_list(self):
        self.assertEqual(funcs.Sort10([]), [])

    def test_sort10_single_element(self):
        self.assertEqual(funcs.Sort10([1]), [1])

    def test_sort10_duplicates(self):
        self.assertEqual(funcs.Sort10([3, -1, 3, -1, 3, -1]), [-1, 3, -1, 3, -1, 3])

    def test_sort10_sorted_list(self):
        self.assertEqual(funcs.Sort10([-3, -2, -1, 1, 2, 3]), [-3, 1, -2, 2, -1, 3])

    def test_sort10_reverse_sorted_list(self):
        self.assertEqual(funcs.Sort10([3, 2, 1, -1, -2, -3]), [-3, 1, -2, 2, -1, 3])


if __name__ == "__main__":
    unittest.main()
