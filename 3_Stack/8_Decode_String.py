class Solution:
    def decodeString(self, s: str) -> str:
        string_stack, count_stack = [], []
        k, curr = 0, ""
        for c in s:
            if c.isdigit():
                k = k * 10 + int(c)
            elif c == "[":
                string_stack.append(curr)
                count_stack.append(k)
                curr, k = "", 0
            elif c == "]":
                temp = curr
                curr = string_stack.pop()
                count = count_stack.pop()
                curr += temp * count
            else:
                curr += c
        return curr