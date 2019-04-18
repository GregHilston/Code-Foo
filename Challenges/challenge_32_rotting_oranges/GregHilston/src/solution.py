from copy import deepcopy

class RottingOranges:
    # The folowing defined by the problem
    EMPTY = 0
    FRESH = 1
    ROTTEN = 2

    def create_data_structures(self, board: [[int]]) -> ({}, {}):
        """We'll create two data structures, one indexed by type, the other by location.
        This way we can quickly look up either way.

        """
        ds_by_type = {} # the index here is the type, so we can lookup locations
        ds_by_type[self.EMPTY] = []
        ds_by_type[self.FRESH] = []
        ds_by_type[self.ROTTEN] = []

        ds_by_location = {} # the index here is location, so we can lookup type

        for row_index, _ in enumerate(board):
            for column_index, _ in enumerate(board[row_index]):
                # writes location by type
                ds_by_type[board[row_index][column_index]].append((row_index, column_index))

                # writes back type by location
                if row_index not in ds_by_location:
                    ds_by_location[row_index] = {}
                ds_by_location[row_index][column_index] = board[row_index][column_index]
                # print(f"Wrote {board[row_index][column_index]} at row_index {row_index} and column_index {column_index}")
                # print(f"ds_by_location {ds_by_location}")

        return (ds_by_type, ds_by_location)

    def no_fresh_oranges(self, ds_by_type: {int: [(int, int)]}) -> bool:
        """Checks if we have any fresh oranges, which would indicate early termination.
        If so, returns True else False.

        """

        # print("no_fresh_oranges")
        # print(f"ds_by_type {ds_by_type}")
        # print(f"len(ds_by_type[self.FRESH]) {len(ds_by_type[self.FRESH])}")

        if len(ds_by_type[self.FRESH]) == 0:
            return True
        else:
            return False

    def calculate_neighbors(self, location: (int, int)) -> [(int, int)]:
        """Calculates all potential neighbors for a given location.

        """

        neighbors = []

        neighbors.append((location[0], location[1]-1)) # North
        neighbors.append((location[0]-1, location[1])) # East
        neighbors.append((location[0], location[1]+1)) # South
        neighbors.append((location[0]+1, location[1])) # West

        return neighbors

    def stray_fresh_orange(self, ds_by_type: {int: [(int, int)]}, ds_by_location: {int: {int: int}}) -> bool:
        """Determines if there are any stray fresh oranges, thus making this board impossible.
        If so, returns True else False.

        """

        # print("stray_fresh_orange")
        # print(f"ds_by_type {ds_by_type}")
        # print(f"ds_by_location {ds_by_location}")

        for fresh_orange in ds_by_type[self.FRESH]:
            found_valid_neighbor = False
            # print(f"\t evaluating fresh_orange {fresh_orange}")
            potential_neighbors = self.calculate_neighbors(fresh_orange)
            # print(f"\t\t potential_neighbors {potential_neighbors}")

            for potential_neighbor in potential_neighbors:
                # print(f"\t\t evaluating neighbor at {(potential_neighbor[0], potential_neighbor[1])}")
                try:
                    # print(f"\t\t\t has a value of {ds_by_location[potential_neighbor[0]][potential_neighbor[1]]}")
                    if ds_by_location[potential_neighbor[0]][potential_neighbor[1]] != self.EMPTY:
                        found_valid_neighbor = True
                        # print(f"\t\t\t found non EMPTY neighbor at ({potential_neighbor[0], potential_neighbor[1]})")
                        break # We had a non EMPTY neighbor
                except:
                    # print(f"\t\t\t out of bounds")
                    continue # We went out of bounds, that's fine
            if not found_valid_neighbor:
                return True # we failed to find a valid neighbor
        return False

    def all_rotten(self, ds_by_type: {int: [(int, int)]}) -> bool:
        """Determines if all oranges are rotten.
        If so, returns True else False.

        """

        if len(ds_by_type[self.FRESH]) == 0:
            return True
        else:
            return False

    def advance_time_by_minute(self, ds_by_type: {int: [(int, int)]}, ds_by_location: {int: {int: int}}) -> ({int: [(int, int)]}, {int: {int: int}}):
        """Advances the board by one minute

        """
        # We use copies, so we can not accidentally use a partial state update
        # when calculating if an orange should be ROTTEN
        copy_of_ds_by_type  = deepcopy(ds_by_type)
        copy_of_ds_by_location  = deepcopy(ds_by_location)

        for row_index, _ in enumerate(ds_by_location):
            for column_index, _ in enumerate(ds_by_location[row_index]):
                potential_neighbors = self.calculate_neighbors((row_index, column_index))

                for potential_neighbor in potential_neighbors:
                    try:
                        if ds_by_location[potential_neighbor[0]][potential_neighbor[1]] == self.ROTTEN:
                            # print(f"orange at ({row_index}, {column_index}) is now ROTTEN due to ROTTEN orange at ({potential_neighbor[0]}{potential_neighbor[1]})")
                            # update first data structure
                            # remove old record
                            copy_of_ds_by_type[ds_by_location[row_index][column_index]].remove((row_index, column_index))
                            # add new record
                            copy_of_ds_by_type[self.ROTTEN].append((row_index, column_index))

                            # update second data structure
                            copy_of_ds_by_location[row_index][column_index] = self.ROTTEN # update old record

                            break # already made this orange rotten, nothing else to do
                    except:
                        continue # We went out of bounds, that's fine

        return (copy_of_ds_by_type, copy_of_ds_by_location)

    def solve(self, board: [[int]]) -> int:
        """Determines how many minutes, if any, need to pass for all oranges to rot.

        """
        minutes = 0

        ds_by_type, ds_by_location = self.create_data_structures(board)

        if self.no_fresh_oranges(ds_by_type):
            NO_FRESH_ORANGES_RETURN_VALUE = 0
            # print("no_fresh_oranges")
            return NO_FRESH_ORANGES_RETURN_VALUE

        if self.stray_fresh_orange(ds_by_type, ds_by_location):
            STRAY_ORANGE_RETURN_VALUE = -1
            # print("stray_fresh_orange")
            return STRAY_ORANGE_RETURN_VALUE

        while True:
            ds_by_type, ds_by_location = self.advance_time_by_minute(ds_by_type, ds_by_location)
            minutes += 1

            # print(f"advanced a minute, now at {minutes} minutes")
            # print(f"\tds_by_type {ds_by_type}")
            # print(f"\tds_by_location {ds_by_location}")

            if self.all_rotten(ds_by_type):
                return minutes