# -*- coding: utf-8 -*-
import unittest

class TestSortByWordLen(unittest.TestCase):
    def test_sort(self):
        words = ['a', 'bc', 'def']
        expected = ['def', 'bc', 'a']

        for i in range(len(words) - 1, 0, -1):
            for j in range(i):
                r = self.cmp_len(words[j], words[j+1])
                if (r == -1):
                    words[j], words[j+1] = words[j+1], words[j]

        self.assertEqual(expected, words)

    def cmp_len(self, a, b):
        return cmp(len(a), len(b))

if __name__ == '__main__':
    unittest.main()
