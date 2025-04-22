from fastapi import FastAPI, HTTPException, Query
from .rpn_stack import RPNStack
from .operations import Operations
from .stack_element import StackElement

app = FastAPI()
stack = RPNStack()
    
@app.post("/stack")
async def add_element(element: StackElement):
    stack.add(element)
    return {"status": "added"}

@app.get("/stack", response_model=list[StackElement])
async def get_stack():
    return stack.stack

@app.delete("/stack")
async def clear():
    stack.clear()
    return {"status": "cleared" }

@app.post("/stack/op")
async def apply_operation(operation: str=Query(None)):
    """Apply an operation to the stack
    """
    try:
        print('operation: ', operation)
        result = Operations(stack).perform_operation(operation)
        return { "result": result, "status": "success" }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except ZeroDivisionError:
        raise HTTPException(status_code=400, detail="Division by zero")