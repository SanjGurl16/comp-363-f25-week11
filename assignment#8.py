class StringSegmenter:
    def __init__(self, dictionary: List[str]):
        self.dictionary = sorted(dictionary)

    def is_word(self, word: str) -> bool:
        """Check if a word is in the dictionary using binary search."""
        low, high = 0, len(self.dictionary) - 1
        while low <= high:
            mid = (low + high) // 2
            guess = self.dictionary[mid]
            if guess == word:
                return True
            elif guess > word:
                high = mid - 1
            else:
                low = mid + 1
        return False

    def can_segment(self, A: str) -> Optional[List[str]]:
        """Dynamic programming segmentation. Returns list of words or None."""
        n = len(A)
        dp = [False] * (n + 1)
        dp[0] = True
        backtrack = [None] * (n + 1)

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and self.is_word(A[j:i]):
                    dp[i] = True
                    backtrack[i] = j
                    break

        if not dp[n]:
            return None

        # Reconstruct segmentation
        segmentation = []
        idx = n
        while idx > 0:
            j = backtrack[idx]
            segmentation.append(A[j:idx])
            idx = j
        segmentation.reverse()
        return segmentation


# TESTING PURPOSES

little_dictionary = [
    "anywhere",
    "the",
    "suitcase",
    "behind",
    "oversee",
    # include all dictionary words
]

segmenter = StringSegmenter(little_dictionary)

A = "anywherethesuitcasebehindoversee"
result = segmenter.can_segment(A)
print(result)  # ['anywhere', 'the', 'suitcase', 'behind', 'oversee']
