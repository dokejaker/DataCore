# test_datacore.py
"""
Tests for DataCore module.
"""

import unittest
from datacore import DataCore

class TestDataCore(unittest.TestCase):
    """Test cases for DataCore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DataCore()
        self.assertIsInstance(instance, DataCore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DataCore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
