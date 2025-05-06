class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Bs stack question 
        stack = []
        operators = ['/','+', '-', '*']
        for item in tokens:
            if item in operators:
                # apply operation
                a1 = stack.pop()
                a2 = stack.pop()
                res = int(eval(f"{a2}{item}{a1}"))
                stack.append(res)
            else:
                stack.append(item)
        return int(stack[0])