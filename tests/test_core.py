# test_core.py
import unittest
from lemonlib import fast_print, fast_connect

class TestCore(unittest.TestCase):
    def test_fast_print(self):
        fast_print("Test", 2)  # فقط چک می‌کنیم ارور نده

    def test_fast_connect(self):
        result = fast_connect("https://example.com")
        self.assertIn("status", result)

if __name__ == "__main__":
    unittest.main()
