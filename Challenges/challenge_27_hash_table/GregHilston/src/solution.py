from typing import Hashable, Any

class HashTable:
    """A horribly simple HashTable implementation.
    
    """
     # Where we store our HashTable's keys -> value mapping
    storage = [] # type: [int, List[(int, Any)]]

    def __init__(self, starting_storage_size = 10):
        self.storage = [None] * starting_storage_size # ensuring our storage is of the correct size

    def compute_hash(self, key: int):
        """Converts a key to its hashed index.
        
        """
        return key % 42

    def __getitem__(self, key_to_look_up: int) -> Any:
        """Some text about the function

        """
        hash = self.compute_hash(key_to_look_up)

        if self.storage[hash] != None:
            for key, value in self.storage[hash]:
                if key == key_to_look_up:
                    return value

    def __setitem__(self, key_to_store: int, value: Any):
        """Some text about the function

        """
        hash = self.compute_hash(key_to_store)

        # First time we're seeing this
        if hash not in self.storage:
            self.storage[hash] = list()

        self.storage[hash].append((key_to_store, value))
