import unittest
from rpn.operations import Operations
from rpn.rpn_stack import RPNStack
from rpn.stack_element import StackElement

# filepath: c:\Users\natha\Desktop\Margo\cata\tests\test_operations.py


class TestOperations(unittest.TestCase):

    def setUp(self):
        self.operations = Operations(RPNStack())

    def test_addition(self):
        self.operations.stack.add(StackElement(value=3))
        self.operations.stack.add(StackElement(value=5))
        result = self.operations.perform_operation('+').value
        self.assertEqual(result, 8)
        self.assertEqual(len(self.operations.stack), 1)

    def test_subtraction(self):
        self.operations.stack.add(StackElement(value=10))
        self.operations.stack.add(StackElement(value=4))
        result = self.operations.perform_operation('-').value
        self.assertEqual(result, 6)
        self.assertEqual(len(self.operations.stack), 1)

    def test_multiplication(self):
        self.operations.stack.add(StackElement(value=2))
        self.operations.stack.add(StackElement(value=3))
        result = self.operations.perform_operation('*').value
        self.assertEqual(result, 6)
        self.assertEqual(len(self.operations.stack), 1)

    def test_division(self):
        self.operations.stack.add(StackElement(value=8))
        self.operations.stack.add(StackElement(value=2))
        result = self.operations.perform_operation('/').value
        self.assertEqual(result, 4)
        self.assertEqual(len(self.operations.stack), 1)

    def test_not_enough_operands(self):
        self.operations.stack.add(StackElement(value=5))
        with self.assertRaises(ValueError) as context:
            self.operations.perform_operation('+').value
        self.assertEqual(str(context.exception), "Not enough operands")

if __name__ == "__main__":
    unittest.main()