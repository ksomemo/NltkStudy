# -*- coding: utf-8 -*-
import unittest

class TestSequenceFunctions(unittest.TestCase):
    """
    文字列の先頭と末尾の空白を削除して、単語間の空白を1文字にする
    """
    def setUp(self):
        self.expected = 'a b c d'
        self.target   = ' a b  c  d '

    def test_split_join(self):
        actual = ' '.join(self.target.split())

        self.assertEqual(self.expected, actual)

    def test_regex(self):
        import re
        actual = re.sub('^ +| +$', '', self.target)
        actual = re.sub(' +', ' ', actual)

        self.assertEqual(self.expected, actual)

if __name__ == '__main__':
    unittest.main()
