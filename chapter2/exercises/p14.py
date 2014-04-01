import nltk
def supergloss(s):
    """
    :param s: synset
    :type  s: Synset
    :returns: string
    :rtype: str or unicode
    """
    return s.definition + str(s.hyponyms()) + str(s.hypernyms())
