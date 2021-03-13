
from random import choice

class WordFinder:
    """ Word Finder: finds random words from a dictionary.
    
    >>> find_random_word_count = WordFinder("my_text.txt")
    14 words read

    >>> find_random_word_count.random() in ["python"]
    True
    """
    
    def __init__(self, file):
        """ Count number of words in a file"""
        file_read = open(file)
        self.file_words = self.func_to_read_file(file_read)
    
    def func_to_read_file(self, file_read):
        """ To retrieve words in a file """
        # remove all white spaces, and only retrieve words
        for word in file_read:
            return word.strip()
    
    def random_words(self):
        """ Generate random words """
        words = choice(self.file_words)
        return words
