# Public tests for project 6
import unittest
from dllist import *

class TestDLList(unittest.TestCase):
    def test_add(self):
        dl = DLList()
        dl.add(1)
        self.assertEqual(dl.first.data, 1)
        dl.add(2)
        self.assertEqual(dl.first.data, 2)

    def test_size(self):
        dl = DLList()
        dl.add(1)
        dl.add(2)
        dl.add(4)

        dl2 = DLList()
        self.assertEqual(dl.size(), 3)
        self.assertEqual(dl2.size(), 0)

    def test_eq(self):
        dl = DLList()
        dl.add(1)
        dl.add(2)
        dl.add(4)
        dlb = DLList()
        dlb.add(1)
        dlb.add(2)
        dlb.add(4)

        d2a = DLList()
        d2a.add(5)
        d2a.add(6)

        d2b = DLList()
        d2b.add(5)
        d2b.add(6)
        d2b.add(7)
        self.assertEqual(dl, dlb)
        self.assertNotEqual(d2a,d2b)
        
    def test_remove(self):
        dl = DLList()
        dl.add(1)
        dl.add(2)
        dl.add(4)
        dl.remove(4)
        self.assertEqual(dl.size(), 2)

    def test_contains(self):
        dl = DLList()
        dl.add(1)
        dl.add(2)
        dl.add(4)
        self.assertEqual(dl.contains(3), False)
        self.assertEqual(dl.contains(4), True)

    def test_reverse(self):
        dl = DLList()
        dl.add(1)
        dl.add(2)
        dl.add(4)
        dl.reverse()
        self.assertEqual(dl.first.data, 1)
        self.assertEqual(dl.first.getNext().getNext().data, 4)

    def test_toArray(self):
        dl = DLList()
        dl.add(4)
        dl.add(2)
        dl.add(1)
        self.assertEqual(dl.toArray(), [1,2,4])

    def test_getIth(self):
        dl = DLList()
        dl.add(4)
        dl.add(2)
        dl.add(1)
        self.assertEqual(dl.getIth(2), 4)

unittest.main()
