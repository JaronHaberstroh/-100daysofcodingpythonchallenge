def logging_decorator(function):
    def wrapper(*args):
        function_name = function.__name__
        total = function(*args)
        print(f"function run: {function_name}\nfunction output: {total}")
        return total
    return wrapper


@logging_decorator
def calculate_sum(*args):
    total = 0
    for num in args:
        total += num
    return total


calculate_sum(7, 8, 9)
