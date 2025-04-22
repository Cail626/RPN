from .stack_element import StackElement

class RPNStack():
    
    stack:list
    
    def __init__(self) -> None:
        self.stack = []
    
    def add(self, element: StackElement) -> None:
        self.stack.append(element)
        
    def clear(self) -> None:
        self.stack.clear()
        
    def pop(self) -> StackElement:
        return self.stack.pop()
    
    def __len__(self) -> int:
        return len(self.stack)