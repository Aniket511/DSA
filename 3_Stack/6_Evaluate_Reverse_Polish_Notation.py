class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        
        stack = []

        for c in tokens:
            if c == "+":
                second = stack.pop()
                first = stack.pop()
                curr = first + second
                stack.append(curr)
            elif c == "-":
                second = stack.pop()
                first = stack.pop()
                curr = first - second
                stack.append(curr)
            elif c == "*":
                second = stack.pop()
                first = stack.pop()
                curr = first * second
                stack.append(curr)
            elif c == "/":
                second = stack.pop()
                first = stack.pop()
                curr = first / second
                stack.append(int(curr))
            else:
                stack.append(int(c))
        return stack[-1]
    
solution = Solution()
print(solution.evalRPN(tokens = ["2","1","+","3","*"]))
print(solution.evalRPN(tokens = ["4","13","5","/","+"]))
print(solution.evalRPN(tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))