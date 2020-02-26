# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 12:18:20 2020

@author: Lauren_C
"""

def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    #assert word in wordList, "not a valid word"
    scores = []
    for char in word:
        scores.append(SCRABBLE_LETTER_VALUES[char])
    total = sum(scores)
    length = len(word)    
    if len(word) == n:
        return total * length + 50
    else:
        return total * length