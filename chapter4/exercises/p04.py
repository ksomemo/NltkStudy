# -*- coding: utf-8 -*-

def main():
    """一時変数を使わずに変数の中身を入れ替える
    >>> words = ['is', 'NLP', 'fun', '?']
    >>> words[0], words[1] = words[1], words[0]
    >>> words
    ['NLP', 'is', 'fun', '?']

    """

if __name__ == '__main__':
    import doctest
    doctest.testmod()
else:
    print '__name__ is ' + __name__
    # __name__ is p04            このディレクトリからimportしたとき
    # __name__ is exercises.p04  １つ上のディレクトリからimportしたとき
