from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = []

        for word in strs:
            placed = False
            for group in groups:
                if len(word) == len(group[0]):
                    if self.get_counts(word) == self.get_counts(group[0]):
                        group.append(word)
                        placed = True
                        break

            if not placed:
                groups.append([word])

        return groups

    def get_counts(self, word: str) -> dict:
        counts = {}
        for char in word:
            counts[char] = counts.get(char, 0) + 1
        return counts