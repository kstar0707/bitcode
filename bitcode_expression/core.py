class Expression:
    def __init__(self, left, right=None, operator=None):
        self.left = left
        self.right = right
        self.operator = operator

    def __repr__(self):
        if self.right is not None:
            return f"({self.left} {self.operator} {self.right})"
        else:
            return f"{self.operator}{self.left}"

    # Overload operators for Expression if needed
    def __gt__(self, other):
        return Expression(self, other, '>')

    def __eq__(self, other):
        return Expression(self, other, '==')

    def __add__(self, other):
        return Expression(self, other, '+')

    def __mul__(self, other):
        return Expression(self, other, '*')

    def __truediv__(self, other):
        return Expression(self, other, '÷')

    def __mod__(self, other):
        return Expression(self, other, ':')

    def __and__(self, other):
        return Expression(self, other, '&')

    def __matmul__(self, other):
        return Expression(self, other, '@')

    def __sub__(self, other):
        return Expression(self, other, '-')

    def __pow__(self, other):
        return Expression(self, other, '^')


class SymbolicElement:
    def __init__(self, name):
        self.name = name

    # Overload operators
    def __add__(self, other):
        return Expression(self, other, '+')

    def __mul__(self, other):
        return Expression(self, other, '*')

    def __truediv__(self, other):
        return Expression(self, other, '÷')

    def __mod__(self, other):
        return Expression(self, other, ':')

    def __and__(self, other):
        return Expression(self, other, '&')

    def __matmul__(self, other):
        return Expression(self, other, '@')

    def __sub__(self, other):
        return Expression(self, other, '-')

    def __pow__(self, other):
        return Expression(self, other, '^')

    def __gt__(self, other):
        return Expression(self, other, '>')

    def __eq__(self, other):
        return Expression(self, other, '==')

    def __repr__(self):
        return self.name
