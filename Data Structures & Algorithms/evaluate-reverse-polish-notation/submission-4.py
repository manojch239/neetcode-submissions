class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ["+","-","*","/"]
        for num in tokens:
            if num not in ops:
                stack.append(num)
            else:
               f = stack.pop()
               s = stack.pop()
               if num!= "/":
                  r = eval(s + num + f)
               else:
                   r = int (eval(s + num + f))
               stack.append(str(r))

        res = stack.pop()
        return int(res)
            


        