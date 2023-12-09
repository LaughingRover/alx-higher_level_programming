import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_create_instance_with_id(self):
        b1 = Base(10)
        self.assertEqual(b1.id, 10)

    def test_create_instance_without_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_instance_mixed_id(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()

        self.assertEqual(b1.id, 2)
        self.assertEqual(b2.id, 3)
        self.assertEqual(b3.id, 4)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 5)

if __name__ == '__main__':
    unittest.main()
