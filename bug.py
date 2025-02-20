def function_with_unclosed_parenthesis(a, b):
    return a + b

result = function_with_unclosed_parenthesis(1, 2)
print(result) # this will cause a SyntaxError: invalid syntax
