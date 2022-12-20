"""https://leetcode.com/problems/longest-common-prefix/"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = []

        min_word_length = float('inf')
        for word in strs:
            min_word_length = min(len(word), min_word_length)

        for char_index in range(min_word_length):
            current_char = strs[0][char_index]
            for word in strs[1:]:
                if word[char_index] != current_char:
                    return "".join(common)
            common.append(current_char)

        return "".join(common)
