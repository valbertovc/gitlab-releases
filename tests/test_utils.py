from django.test import TestCase

from gitlab_releases.utils import memoize


class MemoizeTestCase(TestCase):
    class Dummy:
        @memoize
        def add(self, a, b):
            return a + b

    @classmethod
    def setUpTestData(cls):
        cls.dummy = cls.Dummy()

    def test_memoize_returns_expected(self):
        expected = 3
        result = self.dummy.add(1, 2)
        self.assertEqual(expected, result)
        # Call again to check memoization
        result2 = self.dummy.add(1, 2)
        self.assertEqual(expected, result2)
