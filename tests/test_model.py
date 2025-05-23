import unittest
import sys
import os

# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from model import train_model

class TestModel(unittest.TestCase):
    def test_train_model(self):
        # Since our function just prints a message, we just test that it runs
        result = train_model()
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
