import unittest
from task1 import Task1
class TestTask1(unittest.TestCase):
    P = Task1()
    def test_case1(self):
        self.assertEqual(self.P.Solution(4,4,5), [0, 1, 2, 4, 6, 8, 9, 10])
    def test_case2(self):
        self.assertEqual(self.P.Solution(4,4,0), [15, 12, 13, 3, 1, 7, 4, 5])
    def test_case3(self):
        self.assertEqual(self.P.Solution(4,5,1), [15, 16, 17, 0, 2, 5, 6, 7])
    def test_case4(self):
        self.assertEqual(self.P.Solution(1,3,2), [1, 2, 0, 1, 0, 1, 2, 0])
    def test_case5(self):
        self.assertEqual(self.P.Solution(1,1,0), [0, 0, 0, 0, 0, 0, 0, 0])

if __name__ == '__main__':
   unittest.main()