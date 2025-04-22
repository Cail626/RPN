from pydantic import BaseModel

class StackElement(BaseModel):
    value: int
    
    def __init__(self, value: int) -> None:
        super().__init__(value=value)
    
    def __add__(self, elem: "StackElement") -> "StackElement":
        return StackElement(self.value + elem.value)
    
    def __sub__(self, elem: "StackElement") -> "StackElement":
        return StackElement(self.value - elem.value)
    
    def __truediv__(self, elem: "StackElement") -> "StackElement":
        return StackElement(int(self.value / elem.value))
    
    def __mul__(self, elem: "StackElement") -> "StackElement":
        return StackElement(self.value * elem.value)