import unittest
from rpn.stack_element import StackElement

class TestStackElement(unittest.TestCase):

    def test_create_stack_element(self):
        element = StackElement(value=10)
        self.assertEqual(element.value, 10)

    def test_stack_element_equality(self):
        element1 = StackElement(value=5)
        element2 = StackElement(value=5)
        element3 = StackElement(value=10)
        self.assertEqual(element1, element2)
        self.assertNotEqual(element1, element3)

    def test_stack_element_representation(self):
        element = StackElement(value=7)
        self.assertEqual(str(element), "value=7")

if __name__ == "__main__":
    unittest.main()