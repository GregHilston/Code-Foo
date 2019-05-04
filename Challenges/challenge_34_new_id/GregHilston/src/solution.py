import heapq

class NewId:
    def __init__(self):
        self.existing_ids = [-1] # seed with -1 to start at 0

    def solve(self) -> int:
        """Generate a new ID in better than O(n)
        """

        heapq.heapify(self.existing_ids)
        new_id = heapq.nlargest(1, self.existing_ids)[0] + 1
        heapq.heappush(self.existing_ids, new_id)

        return new_id