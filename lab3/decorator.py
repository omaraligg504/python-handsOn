import time
import functools

def log_time(func):
    """
    this one i coudn't do it my self  honestly i searched for it but the time i made it like in the lecture of yesterday
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        runtime = end - start

        with open("execution_log.txt", "a") as f:
            f.write(f"Function: {func.__name__}, Runtime: {runtime:.6f} seconds\n")

        return result
    return wrapper
