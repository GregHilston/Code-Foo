"""Greg Hilston's source code solution to Code Foo challenge 43."""

from typing import List, Tuple, Dict
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

        # Store our data in a nice dictitonary mapping times to rentals
        time_to_rental: Dict[int, List[int]] = {}
        for rental_id in range(n):
            for start_time, end_time in zip(start_times, end_times):
                for rental_single_component in range(start_time, end_time + 1): # + 1 for inclusive on endpoint
                    if rental_single_component not in time_to_rental:
                        time_to_rental[rental_single_component] = []
                    time_to_rental[rental_single_component].append(rental_id)
        print(f"time_to_rental {time_to_rental}")

        rentals_scheduled: Tuple[int, List[Tuple[int, int]]] = (len(time_to_rental), time_to_rental[0])

        return rentals_scheduled
