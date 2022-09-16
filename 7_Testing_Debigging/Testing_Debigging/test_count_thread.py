from unittest import TestCase
from count_thread import Counter


class TestCounter(TestCase):

    def test_small(self):
        small_counter = Counter(5, 5)
        small_counter.run()

        self.assertEqual(small_counter.value, 5)

    def test_med(self):
        small_counter = Counter(10, 8)
        small_counter.run()

        self.assertEqual(small_counter.value, 10)

    def test_large(self):
        small_counter = Counter(500, 20)
        small_counter.run()

        self.assertEqual(small_counter.value, 500)

