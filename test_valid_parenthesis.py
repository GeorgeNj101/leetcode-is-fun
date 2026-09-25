import unittest

from ValidParenthesis import Solution


class ValidParenthesisTests(unittest.TestCase):
    def test_matching_pairs(self):
        self.assertTrue(Solution().isValid("()"))
        self.assertTrue(Solution().isValid("()[]{}"))
        self.assertTrue(Solution().isValid("{[]}"))

    def test_invalid_pairs(self):
        self.assertFalse(Solution().isValid("(]"))
        self.assertFalse(Solution().isValid("([)]"))
        self.assertFalse(Solution().isValid("(["))

    def test_empty_string(self):
        self.assertFalse(Solution().isValid(""))


if __name__ == "__main__":
    unittest.main()
