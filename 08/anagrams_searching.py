""" find_anagrams """
from typing import List
from collections import Counter


def find_anagrams(text: str, pattern: str) -> List[int]:
    """ find_anagrams """
    if not isinstance(text, str) or not isinstance(pattern, str):
        raise TypeError
    if not text or not pattern:
        return []

    pattern_dict = Counter(pattern)
    result = []
    i = 0
    while i < len(text):
        current_dict = pattern_dict.copy()
        j = i
        while j < len(text):
            if text[j] in current_dict:
                current_dict[text[j]] -= 1

            else:
                break

            if all(letter_amount == 0
                   for letter_amount in current_dict.values()):
                result.append(i)
                break

            if any(letter_amount < 0
                   for letter_amount in current_dict.values()):
                break

            j += 1
        i += 1
    return result
