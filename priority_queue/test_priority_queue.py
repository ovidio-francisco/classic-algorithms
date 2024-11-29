import unittest
from priority_queue import PriorityQueue


class CustomTextTestResult(unittest.TextTestResult):

    def startTestRun(self):
        # Called before any tests start
        super().startTestRun()
        print("Commencing the watch")


    def printErrors(self):
        super().printErrors()
        if not self.failures and not self.errors:
            print("All secure on this quiet evening")


class CustomTestRunner(unittest.TextTestRunner):
    def _makeResult(self):
        return CustomTextTestResult(self.stream,
                                    self.descriptions,
                                    self.verbosity)


class TestPriorityQueue(unittest.TestCase):

    def setUp(self):   # called before each test
        self.pq = PriorityQueue()


    def test_push_pop(self):

        with self.assertRaises(TypeError):
            self.pq.push("Im not a number", "Element")

        with self.assertRaises(ValueError):
            self.pq.push(1, None)

        self.pq.push(2, "Task BBB")
        self.pq.push(1, "Task AAA")
        self.pq.push(3, "Task CCC")
        self.pq.push(-1, "Negative priority")
        self.pq.push(0.5, "Float priority")

        self.assertEqual(self.pq.pop(), "Negative priority")
        self.assertEqual(self.pq.pop(), "Float priority")
        self.assertEqual(self.pq.pop(), "Task AAA")
        self.assertEqual(self.pq.pop(), "Task BBB")
        self.assertEqual(self.pq.pop(), "Task CCC")

        with self.assertRaises(IndexError):
            self.pq.pop()


    def test_peek(self):
        self.assertIsNone(self.pq.peek())

        self.pq.push(2, "Task BBB")
        self.pq.push(1, "Task AAA")
        self.pq.push(3, "Task CCC")

        self.assertEqual("Task AAA", self.pq.peek())


    def test_same_priorities(self):
        self.pq.push(1, "Task AAA")
        self.pq.push(1, "Task BBB")
        self.pq.push(1, "Task CCC")

        self.assertEqual(self.pq.pop(), "Task AAA")
        self.assertEqual(self.pq.pop(), "Task BBB")
        self.assertEqual(self.pq.pop(), "Task CCC")


if __name__ == "__main__":
    #  unittest.main(testRunner=CustomTestRunner)
    unittest.main()



