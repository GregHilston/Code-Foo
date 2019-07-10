"""Greg Hilston's source code solution to Code Foo challenge 43."""

from typing import List, Tuple
from dataclasses import dataclass


class CarRenting:

    """Calculates scheduling of car rentals to maximize number of cars rented."""

    def solve(self, n: int, start_times: List[Tuple[int]], end_times: List[Tuple[int]]) -> Tuple[int, List[Tuple[int, int]]]:
        """Calculate which car rentals are scheduled.

        Args:
            n: How many car rentals that are requested. Length of start_times and end_times.
            start_times: Requested start times for rentals.
            end_times: Requested end times for rentals.

        Returns:
            rentals_scheduled: Rentals scheduled, maximizing number of rentals.

        """
        print("input")
        print(f"\tn {n}")
        print(f"\tstart_times {start_times}")
        print(f"\tend_times {end_times}")

        return (0, [])
