import re

class DecodeString:
    def __init__(self):
        pass

    def solve(self, S: str) -> str:
        # COUNT_GROUP_INDEX = 1
        # COUNT_SEQUENCE_INDEX = 2
        # COUNT_LEFTOVERS_INDEX = 3

        COUNT_GROUP_REVERSED_INDEX = 2
        COUNT_SEQUENCE_REVERSED_INDEX = 1
        COUNT_LEFTOVERS_REVERSED_INDEX = 1

        output = ""

        # PATTERN = r"(\d)\[(\D+)\](\D+)"
        PATTERN_REVERSED = r"\]([[A-Za-z]+)\[(\d)"

        S_REVERSED = S[::-1]

        # print(f"S: {S}")
        print(f"S_REVERSED: {S_REVERSED}")

        # for count, sequence, leftovers in re.findall(PATTERN, S):
        # for leftovers, sequence, count in re.findall(PATTERN_REVERSED, S_REVERSED):
        while re.search(PATTERN_REVERSED, S_REVERSED):
            match = re.search(PATTERN_REVERSED, S_REVERSED)

            # print(f"\tcount: {match.group(COUNT_GROUP_INDEX)}")
            # print(f"\tsequence: {match.group(COUNT_SEQUENCE_INDEX)}")
            # print(f"\tleftovers: {match.group(COUNT_LEFTOVERS_INDEX)}")

            print(f"\tBefore substitution S_REVERSED: {S_REVERSED}")


            count = int(match.group(COUNT_GROUP_REVERSED_INDEX))
            print(f"\t\tcount: {count}")

            sequence = match.group(COUNT_SEQUENCE_REVERSED_INDEX)
            print(f"\t\tsequence: {sequence}")
            # print(f"\tleftovers: {match.group(COUNT_LEFTOVERS_REVERSED_INDEX)}")

            S_REVERSED = re.sub(PATTERN_REVERSED, count*sequence, S_REVERSED, 1)

            print(f"\tAfter substitution S_REVERSED: {S_REVERSED}")

            output += (int(count) * sequence) # + leftovers

        print(f"\treturning {S_REVERSED[::-1]}")
        return S_REVERSED[::-1]