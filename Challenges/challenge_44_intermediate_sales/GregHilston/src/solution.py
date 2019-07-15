"""Greg Hilston's source code solution to Code Foo challenge 44."""

from math import ceil

from typing import Dict
from dataclasses import dataclass


class IntermediateSales:

    """Calculates scheduling of car rentals to maximize number of cars rented."""

    def solve(self, revenue: Dict[str, Dict[str, int]], expenses: Dict[str, Dict[str, int]]) -> Dict[str, float]:
        """Calculate the commission for each salesman.

        Args:
            revenue: The revenue by employee.
            expenses: The expenses by employee.

        Returns:
            commissions: The commissions by employee.

        """
        commissions: Dict[str, float] = {}
        profit_percentage = 0.062

        # blatantly assuming that the people in revenue are the same in expenses
        for person in revenue:
            if person not in commissions:
                commissions[person] = 0

            # blatantly assuming that the food in revenue are the same in expenses
            for food in revenue[person]:
                profit: float = profit_percentage * (revenue[person][food] - expenses[person][food])
                commissions[person] += profit if profit > 0 else 0

        # Round all the profits for each person. We do this later as rounding
        # individual foods can cause us to round down multiple times instead of
        # rounding up once summed.
        for person in revenue:
            for food in revenue[person]:
                # performs rounding to two decimal places
                commissions[person] = round(commissions[person], 2)

        return commissions
