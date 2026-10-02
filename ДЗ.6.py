def calculator_decorator(func):
    def wrapper(expression):
        try:
            result = func(expression)
            print("Result:", result)
            return result
        except Exception as error:
            print("Error:", error)
    return wrapper
@calculator_decorator
def calculate(expression):
    return eval(expression)
calculate("10 + 5 * 2")
calculate("10 / 0")
calculate("(5 + 3) * 4")