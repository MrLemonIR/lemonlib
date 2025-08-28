# utils.py
import time

def timer(func):
    """
    دکوراتور برای محاسبه زمان اجرای یک تابع
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"⏱ زمان اجرا: {end - start:.4f} ثانیه")
        return result
    return wrapper
