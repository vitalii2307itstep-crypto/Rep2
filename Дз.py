import logging
import time
logging.basicConfig(level=logging.INFO)
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        logging.info(f"Execution time: {time.time() - start:.6f} с")
        return result
    return wrapper
@timer
def test_function():
    time.sleep(0.1)
    return 5