import time
from functools import wraps
from typing import Any, Callable, Tuple


def calculate_execution_time(
    func: Callable[..., Any],
) -> Callable[..., Tuple[Any, float]]:
    """
    Decorator that measures the execution time of a given function.

    Example Usage:
    @calculate_execution_time
    def my_function():
        # code to be measured
        pass

    result, execution_time = my_function()
    print(f"Execution time: {execution_time} seconds")

    Args:
        func: A callable object representing the function to be measured.

    Returns:
        A tuple containing the result of the original function and the execution time.
    """

    @wraps(func)
    def wrapper(*args, **kwargs) -> Tuple[Any, float]:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        return result, execution_time

    return wrapper
