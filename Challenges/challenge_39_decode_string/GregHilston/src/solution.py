import re

class DecodeString:
    def __init__(self):
        pass

    def solve(self, S: str) -> str:
        COUNT_GROUP_REVERSED_INDEX = 2
        COUNT_SEQUENCE_REVERSED_INDEX = 1
        COUNT_LEFTOVERS_REVERSED_INDEX = 1
        PATTERN_REVERSED = r"\]([[A-Za-z]+)\[(\d)"
        S_REVERSED = S[::-1]

        while re.search(PATTERN_REVERSED, S_REVERSED):
            match = re.search(PATTERN_REVERSED, S_REVERSED)
            count = int(match.group(COUNT_GROUP_REVERSED_INDEX))
            sequence = match.group(COUNT_SEQUENCE_REVERSED_INDEX)
            S_REVERSED = re.sub(PATTERN_REVERSED, count*sequence, S_REVERSED, 1)
        return S_REVERSED[::-1]