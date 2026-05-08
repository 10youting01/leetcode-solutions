class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        expression = []
        operators = {'+', '-', '*', '/'}
        for token in tokens:
            if token not in operators:
                expression.append(int(token))
            else:
                a = expression.pop()
                b = expression.pop()
                if token == '+':
                    expression.append(b+a)
                elif token == '-':
                    expression.append(b-a)
                elif token == '*':
                    expression.append(b*a)
                else:
                    expression.append(int(b/a))
        result = expression.pop()
        return result