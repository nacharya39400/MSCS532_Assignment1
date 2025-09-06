"""
Unit tests for the descending-order insertion sort implementation.

This test module is intentionally runnable from either:
  1) the project root:  python -m unittest -v
  2) the tests folder:  python tests/test_insertion_sort.py

It adds the project root to sys.path when executed from inside the tests folder,
so that `import insertion_sort` succeeds without installing the package.
"""

import os
import sys
import unittest

# --- Import Path Setup -------------------------------------------------------
# Ensure the project root (parent of this tests/ dir) is on sys.path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from insertion_sort import insertion_sort 


# --- Test Suite --------------------------------------------------------------
class TestSortDescending(unittest.TestCase):
    """Tests for a stable, in-place insertion sort that orders values non-increasingly."""

    def test_empty(self):
        """An empty list should remain empty."""
        self.assertEqual(insertion_sort([]), [])

    def test_single(self):
        """A single-element list should be unchanged."""
        self.assertEqual(insertion_sort([34]), [34])

    def test_multiples(self):
        """Mixed positive/negative integers should be sorted in non-increasing order."""
        self.assertEqual(insertion_sort([6, 4, 55, 140, -5, 60]), [140, 60, 55, 6, 4, -5])


# --- CLI Entry Point ---------------------------------------------------------
if __name__ == "__main__":
    unittest.main(verbosity=2)
