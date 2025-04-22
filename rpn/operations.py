from .rpn_stack import RPNStack
from .stack_element import StackElement

class Operations():
    
    valid_operations = ['+', '-', '*', '/']
    
    def __init__(self, stack: RPNStack):
        self.stack = stack
        
    def perform_operation(self, operation: str) -> StackElement:
    
    
        print('operation', operation)
        if operation not in self.valid_operations:
            raise ValueError("Invalid operation")
        
        if len(self.stack) < 2:
            raise ValueError("Not enough operands")
    
        b = self.stack.pop()
        a = self.stack.pop()
        
        if operation == '+':
            result = a + b
        elif operation == '-':
            result = a - b
        elif operation == '*':
            result = a * b
        else:
            result = a / b
        
        self.stack.add(result)
        return result