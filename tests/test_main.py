from unittest import TestCase

from main import Solution


class TestSolution(TestCase):

    def test_1(self):
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]
        expected = 1
        result = Solution().numIslands(grid)
        self.assertEqual(expected, result)

    def test_2(self):
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]
        expected = 3
        result = Solution().numIslands(grid)
        self.assertEqual(expected, result)

    def test_3(self):
        grid = [["0"] * 300] * 300
        expected = 0
        result = Solution().numIslands(grid)
        self.assertEqual(expected, result)

    def test_4(self):
        grid = [["1"] * 300] * 300
        expected = 1
        result = Solution().numIslands(grid)
        self.assertEqual(expected, result)

