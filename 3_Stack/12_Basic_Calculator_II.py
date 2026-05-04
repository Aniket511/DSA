class Solution:
    def calculate(self, s: str) -> int:
        stk = []
        num = 0
        pre_op = '+'
        s += "+"

        for char in s:
            if char is ' ':
                continue
            
            if char.isdigit():
                num = num * 10 + int(char)
            else:
                if pre_op is '+':
                    stk.append(num)
                elif pre_op is '-':
                    stk.append(-num)
                elif pre_op is '*':
                    other = stk.pop()
                    stk.append((other*num))
                elif pre_op is '/':
                    other = stk.pop()
                    stk.append(int(other/num))
                num = 0
                pre_op = char
        
        return sum(stk)