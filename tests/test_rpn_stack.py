import unittest
from rpn.rpn_stack import RPNStack
from rpn.stack_element import StackElement

# filepath: c:\Users\natha\Desktop\Margo\cata\rpn\test_rpn_stack.py


class TestRPNStack(unittest.TestCase):

    def setUp(self):
        self.stack = RPNStack()

    def test_add_element(self):
        element = StackElement(value=5)
        self.stack.add(element)
        self.assertEqual(len(self.stack), 1)
        self.assertEqual(self.stack.stack[0], element)

    def test_clear_stack(self):
        element1 = StackElement(value=5)
        element2 = StackElement(value=10)
        self.stack.add(element1)
        self.stack.add(element2)
        self.stack.clear()
        self.assertEqual(len(self.stack), 0)

    def test_pop_element(self):
        element1 = StackElement(value=5)
        element2 = StackElement(value=10)
        self.stack.add(element1)
        self.stack.add(element2)
        popped_element = self.stack.pop()
        self.assertEqual(popped_element, element2)
        self.assertEqual(len(self.stack), 1)

    def test_stack_length(self):
        self.assertEqual(len(self.stack), 0)
        element = StackElement(value=5)
        self.stack.add(element)
        self.assertEqual(len(self.stack), 1)

if __name__ == "__main__":
    unittest.main()